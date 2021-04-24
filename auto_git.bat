cd C:\Users\Shun\github\atcoder
git init
git config --global user.name "ishisun"
git config --global user.email "d.logicool.a@gmail.com"
git clone git@github.com:ishisun/atcoder.git C:\Users\Shun\github\atcoder\atcoder
xcopy /d /e C:\Users\Shun\Documents\atcoder C:\Users\Shun\github\atcoder\atcoder
cd atcoder
git add --all
git commit -m "auto commit"
git push -f
pause
