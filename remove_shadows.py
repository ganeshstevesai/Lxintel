import os
import re

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

for file in css_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove all text-shadow declarations (single-line)
        content = re.sub(r'text-shadow\s*:[^;]+;', 'text-shadow: none;', content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Removed all text-shadow from every CSS file.")
