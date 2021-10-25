import os

print("First commit")
os.system('git add -A && git commit -m "Initial commit"')

url = "{{cookiecutter.repo_url}}"
if url: 
    os.system('git push')
