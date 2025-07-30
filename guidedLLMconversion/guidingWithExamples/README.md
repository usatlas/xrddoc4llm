# guidingWithExamples
This contains conversions into md format using examples of a manually edited conversion for LLMs to base their product off of in attempt to guide LLMs to produce what is desired.

## Sections
- *originalDocs* contains original docx that were converted to HTML. It was converted from a doc first because the sections were easier to extract in docs than in the original HTML.
- *htmls* contains the html converted from the docs.
- *mds* contains all the MarkDown documents that were converted from HTML.
    - [sec3.4-original.md](mds/sec3.4-original.md) is the original MarkDown for section 3.4 produced prior to the revisions.
    - [sec3.4-revised.md](mds/sec3.4-revised.md) is the mannually revised version of the original and used as the example for the LLMs to follow.
    - *usingExample* contains the MarkDown results from the respective LLMs using an example to guide them.
    - *withoutExample* contains the MarkDown results from the respective LLMs without using the examples to guide them. 
- [extraInformation.md](extraInformation.md) contains notes taken throughout the process of converting, including the prompt used and the main focuses when manually editing the example and other notable pieces of information.