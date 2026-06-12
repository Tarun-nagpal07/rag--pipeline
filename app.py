import chainlit as cl

from src.graph.build import graph


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("retrieval_history", [])

    await cl.Message(
        content="""
🏥 Health & Fitness RAG Assistant

Ask questions about:
• Fitness
• Nutrition
• Wellness
• Healthy lifestyle

Retrieved chunks, similarity scores and RAGAS metrics will appear in the sidebar.
"""
    ).send()


@cl.on_message
async def on_message(message: cl.Message):

    msg = cl.Message(content="Thinking...")
    await msg.send()

    try:

        result = graph.invoke(
            {
                "messages": [
                    (
                        "user",
                        message.content
                    )
                ]
            }
        )

        answer = result["messages"][-1].content

        chunks = result.get("context", [])

        ragas_scores = result.get(
            "ragas_scores",
            {}
        )

        # ---------------------------------
        # CHUNK HISTORY
        # ---------------------------------

        retrieval_history = cl.user_session.get(
            "retrieval_history",
            []
        )

        scores = []

        chunk_report = []

        chunk_report.append(
            f"\n# Question\n{message.content}\n"
        )

        for idx, chunk in enumerate(chunks, start=1):

            score = float(
                chunk.get("score", 0)
            )

            scores.append(score)

            chunk_report.append(
                f"""
## Chunk {idx}

Similarity Score: {score:.3f}

{chunk.get("content", "")}

-----------------------------------
"""
            )

        avg_score = (
            sum(scores) / len(scores)
            if scores
            else 0
        )

        chunk_report.append(
            f"""

## Retrieval Summary

Average Similarity Score: {avg_score:.3f}

"""
        )

        retrieval_history.append(
            "\n".join(chunk_report)
        )

        cl.user_session.set(
            "retrieval_history",
            retrieval_history
        )

        # ---------------------------------
        # SIDEBAR: ALL CHUNKS
        # ---------------------------------

        chunks_panel = cl.Text(
            name="Retrieved Chunks",
            content="\n\n".join(
                retrieval_history
            ),
            display="side"
        )

        # ---------------------------------
        # SIDEBAR: RAGAS
        # ---------------------------------

        ragas_panel = cl.Text(
            name="RAGAS Scores",
            content=f"""
# RAGAS Evaluation

Faithfulness:
{ragas_scores.get("faithfulness", 0):.3f}

Context Relevance:
{ragas_scores.get("context_relevance", 0):.3f}

Answer Relevancy:
{ragas_scores.get("answer_relevancy", 0):.3f}
""",
            display="side",
        )

        msg.content = answer
        msg.elements = [
            chunks_panel,
            ragas_panel,
        ]

        await msg.update()

    except Exception as e:

        msg.content = f"❌ Error: {str(e)}"
        await msg.update()