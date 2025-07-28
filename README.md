# The xrddoc4llm Project Repo

This repository containes works that transform [Xrootd Referece Documents](https://xrootd.org/docs.html) to formats preferred by Large Language Models. 

# Sections:

- [llm-experimentation](llm-experimentation/README.md) contains initial comparisons of LLM performance in converting documentation to a markdown format. It also containts a [script](llm-experimentation/scripts/) to algorithmically convert the documentation into a MD format.
- [ragsystem](ragsystem/README.md) contains two versions of a simple RAG system that ChromaDB and embedding models to query the converted documentation. Each version contains an MCP server that can be used to query the documents. They share a single documentation folder that contains the converted documentation (3 documents at the moment). 
  - [local-encoding](ragsystem/local-encoding/) uses a local LLM to query and embed the documents.
  - [gemini-encoding](ragsystem/gemini-encoding/) uses the Gemini API to query and embed the documents.
