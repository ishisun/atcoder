cd C:\Users\Shun\github\atcoder
git init
git config --global user.name "I_S"
git config --global user.email "d.logicool.a@gmail.com"
git clone https://github.com/ishisun/atcoder C:\Users\Shun\github\atcoder\atcoder
xcopy /d C:\Users\Shun\Documents\atcoder C:\Users\Shun\github\atcoder\atcoder
cd atcoder
git add --all
git commit -m "auto commit"
git push -f
pause