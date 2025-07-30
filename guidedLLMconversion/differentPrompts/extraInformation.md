# Extra Information

Information that'll clarify the process and results, also adding other thoughts. 

### Note: 
>*opened using VS Code and cmd-shft-v to view*

>*used free account for all*

## Prompts:

1. *"Convert this entire file into all raw MarkDown code so it's LLM friendly"*
2. *"Convert this entire file into all raw MarkDown code and enhance it so it feels more modern and minimal"*
3. I decided not to proceed with this prompt, since it asked the LLMs to change color or font, both of which MarkDown is incapable of.
4. *"Convert this entire file into all raw MarkDown code and add features to make it more useful and interactive"*
5. *"Convert this entire file into all raw MarkDown code and reformat it to make it more readable and maintainable"*
6. *"Convert this entire file into all raw MarkDown code. Then pretend you're the lead dev on this project and change the MarkDown code to make 3 improvements you would prioritize to increase quality or user satisfaction"*

## LLMs used + notes:


- **Google Gemini** (commercial)
    - can not handle large files 
    - unable to generate files (limited production)
- **ChatGPT** (commercial)
    - can process large files
    - able to generate files
    - occasional raw code formatting issues (ex. blank spaces)
- **Microsoft Copilot** (commercial)
    - can not process HTML 
        - to remedy this, converted the code to pdf or copy and pasted it if shorter
    - able to process large files but unable to produce as large of a file
        - able to produce it in parts (entire xrootd references in 9 parts) (**v2**)
            - missed a lot of content
- **Deepseek** (commercial)
    - only able to read small portions of large files (16% of the entire xrootd references)
    - hard to produce raw code (not parsed)
- **Ollama** (local)
    - simple, did not change much with different prompts