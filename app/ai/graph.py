from typing import Annotated,TypedDict
from langchain_core.messages import BaseMessage,HumanMessage,SystemMessage
from langgraph.graph import StateGraph,END
from langgraph.prebuilt import ToolNode,tools_condition
from langchain_google_genai import ChatGoogleGenerativeAI
from app.config import GEMINI_API_KEY,GEMINI_MODEL
from app.ai.tools import TOOLS
from app.ai.vector_store import search_knowledge
class State(TypedDict): messages:Annotated[list[BaseMessage],'messages']
_graph=None
def build_graph():
    if not GEMINI_API_KEY: raise RuntimeError('GEMINI_API_KEY is missing')
    model=ChatGoogleGenerativeAI(model=GEMINI_MODEL,google_api_key=GEMINI_API_KEY,temperature=.2).bind_tools(TOOLS)
    def assistant(s):
        ctx='\n'.join(search_knowledge(s['messages'][-1].content))
        sys=SystemMessage(content='You are a professional student database assistant. Use database tools for actual student records and never invent data. Use project context for general questions.\n'+ctx)
        return {'messages':[model.invoke([sys]+s['messages'])]}
    g=StateGraph(State);g.add_node('assistant',assistant);g.add_node('tools',ToolNode(TOOLS));g.set_entry_point('assistant');g.add_conditional_edges('assistant',tools_condition,{'tools':'tools',END:END});g.add_edge('tools','assistant');return g.compile()
def ask_chatbot(message):
    global _graph
    if _graph is None:
        _graph = build_graph()

    result = _graph.invoke(
        {'messages': [HumanMessage(content=message)]}
    )

    content = result['messages'][-1].content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, str):
                text_parts.append(item)
            elif isinstance(item, dict) and 'text' in item:
                text_parts.append(item['text'])

        return '\n'.join(text_parts)

    return str(content)