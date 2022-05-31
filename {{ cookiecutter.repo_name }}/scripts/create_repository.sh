gh repo create "betrybe/{{ cookiecutter.repo_name }}" --private
git init
git add . && git commit -m "init"
git branch -M main
git remote add origin https://github.com/betrybe/{{ cookiecutter.repo_name }}.git
git push -u origin main 
