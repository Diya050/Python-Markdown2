import markdown2

text = "Here is a math formula: $$A^2 + B^2$$\n\nThis is an organic chemical equation: $$C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O$$\n\nThe chemical structure can be represented as:\n\n```\n    H\n    |\nH---C---H\n|   |   |\nH---C---H\n    |    \n    C---H\n    |\n    H\n```\n"

mathjax_config = {
    "TeX": {"equationNumbers": {"autoNumber": "AMS"}},
    "extensions": ["tex2jax.js"],
}

html = markdown2.markdown(text, extras=["fenced-code-blocks", "mathjax", "cuddled-lists", "code-friendly"])
html = f"<!DOCTYPE html>\n<html>\n<head>\n    <meta charset=\"utf-8\">\n    <script type=\"text/x-mathjax-config\">\n        MathJax.Hub.Config({mathjax_config});\n    </script>\n    <script type=\"text/javascript\" src=\"https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\">\n    </script>\n</head>\n<body>\n{html}\n</body>\n</html>"

print(html)
