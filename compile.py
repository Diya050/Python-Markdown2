import markdown2

md = markdown2.markdown("""
This is a brief overview of the compilation process in C.

# Preprocessor

The preprocessor performs macro substitution and file inclusion. The output of this stage is a modified C file.

# Compiler

The compiler takes the modified C file and generates assembly code. The output of this stage is an assembly file.

```mermaid
graph LR;
    A(Original C File) -->B((Preprocessor));
    B -->C[Modified C File];
    C(Modified C File) --> D{Compiler};
    D --> E[Assembly File];
    E(Assembly File) --> F{{Assembler}};
    F --> G[Object File];
    G((Object Files)) --> H{{Linker}};
    H --> I(Executable File);

```
# Assembler

The assembler takes the assembly file and generates an object file. The output of this stage is an object file.

# Linker

The linker takes one or more object files and generates an executable file. The output of this stage is an executable file.



""", extras=['fenced-code-blocks', 'mermaid', 'tables'])

html_header = """<!DOCTYPE html>
<html>
  <head>
    <style>

    .mermaid-pre {
        visibility: hidden;
    }
    </style>
  </head>
  <body>
    <h1>Compilation Process in C</h1>
"""

html_footer = """    <script type="module" defer>
      import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@9/dist/mermaid.esm.min.mjs';
      mermaid.initialize({
        securityLevel: 'loose',
        startOnLoad: true
      });
      let observer = new MutationObserver(mutations => {
        for(let mutation of mutations) {
          mutation.target.style.visibility = "visible";
        }
      });
      document.querySelectorAll("pre.mermaid-pre div.mermaid").forEach(item => {
        observer.observe(item, { 
          attributes: true, 
          attributeFilter: ['data-processed'] });
      });
    </script>
  </body>
</html>
"""

html = html_header + md + html_footer

fp = "compile.html"
with open(fp, "w+", newline="", encoding="UTF-8") as f:
    f.write(html)
