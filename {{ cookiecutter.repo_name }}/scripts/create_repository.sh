gh repo create "acnaweb/{{ cookiecutter.repo_name }}" --private
git init
git add . && git commit -m "init"
git branch -M main
git remote add origin https://github.com/acnaweb/{{ cookiecutter.repo_name }}.git
git push -u origin main 
