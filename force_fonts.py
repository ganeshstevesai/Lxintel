import os

css_files = [
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\static\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\settlement\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Medical summary\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\injury\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\FAA_Medcert\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\Demand QA\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\demand Optimizer\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\casevalue\index.css",
    r"c:\Users\Admin\Pictures\all_project\Lxintel\Lxintel\book_builder\index.css",
]

global_styles = """
/* Global Font & Color Overrides */
body, html, p, span, div, input, button, a, label, li, td, th {
    font-family: "Montserrat", sans-serif !important;
    color: #0d6efd !important;
}

h1, h2, h3, h4, h5, h6, .card-title, .header-title h1, .topbar-logo span {
    font-family: "Cormorant Garamond", serif !important;
    color: #0d6efd !important;
}
"""

for file in css_files:
    if os.path.exists(file):
        with open(file, 'a', encoding='utf-8') as f:
            f.write(global_styles)

print("Appended global font styles and color overrides to all CSS files")
