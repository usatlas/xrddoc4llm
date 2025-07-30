# Extra Information
This contains extra information that can help with understanding the information presented in guidingWithExamples. 

## Process:
1. Isolated section 3.4 in xrd_config.docx in the xrddocs drive
2. Saved that portion as an html (sec3.4.html)
3. Asked LLM to convert it to MarkDown code (sec3.4-original.md)
4. Manually revised the MarkDown code to be as similar to the actual html (to the best of my ability) (sec3.4-revised.md)
5. Used the revised version as an example for LLMs to convert a different section (3.5) into md

### Prompts:
**If short enough**:   

    The following is an example of converting an html file to markdown file  
    --------------- Begin of the original HTML file ----------  
    <sec3.4.html text>  
    --------------- The end of the original HTML file -----------  
    --------------- Begin of the converted Markdown file ----------  
    <sec3.4.md text>  
    --------------- The end of the converted Markdown file ----------  
    Use the above example, convert the following html file to a markdown file  
    <sec3.5.html text>  

**If above exceeded the word limit**:  

    The following is an example of converting an html file to markdown file. The files sec3.4.html and sec3.4-revised.md are an example of converting an html file (sec3.4.html) to markdown file (sec3.4-revised.md)
    Use the above example, and convert the sec3.5.html html file to a markdown file ike the example did.

## Notes

### Revising:  
- LLM adds extra lines between text sections (visible in the unrevised md)
- adding in italicization and bolding that was either messed up or forgotten

### Conversion of section 3.5:
- only used 3 LLMs (all commercial) (ChatgGPT, Gemini, and Deepseek) because Copilot and Ollama were unable to process HTML files
- ChatGPT was relatively accurate, only having a few formatting issues with bolding and italicizing (compare the produced md file using the example as a guide and without)
- Deepseek did well with formatting but changed/simplified a few notes at the bottom of 3.5 when given an example
- Gemini's formatting was good when it came to bolding and italicising, but it occasionally wasn't able to create new lines where there should've been
- Overall there are differences in using an example compared to not, but those differences are relatively minimal although still prevalent.