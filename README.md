saneechka@MacBook-Pro-Aleksandr ~ % cd 353501_Zagreshchenko_7 
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint:
hint: 	git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint: 	git branch -m <name>
Инициализирован пустой репозиторий Git в /Users/saneechka/353501_Zagreshchenko_7/.git/
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch IGI
fatal: not a valid object name: 'master'
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % nano README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "added README"
[master (корневой коммит) e34c189] added README
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI
Переключились на ветку «IGI»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mkdir IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd IGI   
saneechka@MacBook-Pro-Aleksandr IGI % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr IGI % ls
saneechka@MacBook-Pro-Aleksandr IGI % git add .gitkeep
saneechka@MacBook-Pro-Aleksandr IGI % git commit 
подсказка: Ожидание, пока вы закроете редактор с файлом... 
zsh: suspended  git commit
saneechka@MacBook-Pro-Aleksandr IGI % git commit -m ".gitkeep"
[IGI abdce26] .gitkeep
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 IGI/.gitkeep
saneechka@MacBook-Pro-Aleksandr IGI % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd
saneechka@MacBook-Pro-Aleksandr ~ % cd 353501_Zagreshchenko_7/IGI
saneechka@MacBook-Pro-Aleksandr IGI % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b STRWEB
Переключились на новую ветку «STRWEB»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mkdir STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md	STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd STRWEB 
saneechka@MacBook-Pro-Aleksandr STRWEB % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr STRWEB % git add .gitkeep
saneechka@MacBook-Pro-Aleksandr STRWEB % git commit -m "gk:
dquote> 
dquote>  
saneechka@MacBook-Pro-Aleksandr STRWEB % git commit -m "gk"
[STRWEB c00a069] gk
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 STRWEB/.gitkeep
saneechka@MacBook-Pro-Aleksandr STRWEB % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git statua
git: «statua» не является командой git. Смотрите «git --help».

Самые похожие команды:
	status
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git status
Текущая ветка: STRWEB
нечего коммитить, нет изменений в рабочем каталоге
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git remote add origin https://github.com/saneechka/353501_Zagreshchenko.git
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 9, готово.
Подсчет объектов: 100% (9/9), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (5/5), готово.
Запись объектов: 100% (9/9), 698 байтов | 698.00 КиБ/с, готово.
Total 9 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI -> IGI
 * [new branch]      STRWEB -> STRWEB
 * [new branch]      master -> master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
  IGI
* STRWEB
  master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf IGI
Password:
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "removed IGI from STRWEB"
[STRWEB a9e1dd4] removed IGI from STRWEB
 1 file changed, 0 insertions(+), 0 deletions(-)
 delete mode 100644 IGI/.gitkeep
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin 
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (2/2), 288 байтов | 288.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   c00a069..a9e1dd4  STRWEB -> STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI_LR1
Переключились на новую ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd IGI
cd: no such file or directory: IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md	STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout master
Переключились на ветку «master»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI
fatal: a branch named 'IGI' already exists
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout  IGI  
Переключились на ветку «IGI»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd IGI 
saneechka@MacBook-Pro-Aleksandr IGI % ls
saneechka@MacBook-Pro-Aleksandr IGI % git checkout -b IGI_LR1
fatal: a branch named 'IGI_LR1' already exists
saneechka@MacBook-Pro-Aleksandr IGI % git branch
* IGI
  IGI_LR1
  STRWEB
  master
saneechka@MacBook-Pro-Aleksandr IGI % git branch delete IGI_LR1 
saneechka@MacBook-Pro-Aleksandr IGI % git branch               
* IGI
  IGI_LR1
  STRWEB
  delete
  master
saneechka@MacBook-Pro-Aleksandr IGI % git branch -d IGI_LR1 delete
error: the branch 'IGI_LR1' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D IGI_LR1'
hint: Disable this message with "git config advice.forceDeleteBranch false"
error: the branch 'delete' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D delete'
hint: Disable this message with "git config advice.forceDeleteBranch false"
saneechka@MacBook-Pro-Aleksandr IGI % git branch -D IGI_LR1 delete
Ветка IGI_LR1 удалена (была a9e1dd4).
Ветка delete удалена (была a9e1dd4).
saneechka@MacBook-Pro-Aleksandr IGI % ls
saneechka@MacBook-Pro-Aleksandr IGI % git branch
* IGI
  STRWEB
  master
saneechka@MacBook-Pro-Aleksandr IGI % git checkout -b IGI_LR1
Переключились на новую ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr IGI % mkdir LR1
saneechka@MacBook-Pro-Aleksandr IGI % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr IGI % git add .
saneechka@MacBook-Pro-Aleksandr IGI % git commit -m "creare IGI_LR1"
Текущая ветка: IGI_LR1
нечего коммитить, нет изменений в рабочем каталоге
saneechka@MacBook-Pro-Aleksandr IGI % ls
LR1
saneechka@MacBook-Pro-Aleksandr IGI % cd LR1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
saneechka@MacBook-Pro-Aleksandr LR1 % ls -a
.	..
saneechka@MacBook-Pro-Aleksandr LR1 % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr LR1 % git add .                     
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "creare IGI_LR1"
[IGI_LR1 e0c7748] creare IGI_LR1
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 IGI/LR1/.gitkeep
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (3/3), готово.
Запись объектов: 100% (3/3), 353 байта | 353.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'IGI_LR1' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/IGI_LR1
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI_LR1 -> IGI_LR1
saneechka@MacBook-Pro-Aleksandr LR1 % cd ..
saneechka@MacBook-Pro-Aleksandr IGI % ls
LR1
saneechka@MacBook-Pro-Aleksandr IGI % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv IGI/L1/ 353501_Zagreshchenko_1
mv: rename IGI/L1/ to 353501_Zagreshchenko_1: No such file or directory
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv IGI/L1/ 353501_Zagreshchenko_7
mv: rename IGI/L1/ to 353501_Zagreshchenko_7: No such file or directory
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv IGI/LR1/ 353501_Zagreshchenko_7
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % la                                
zsh: command not found: la
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
353501_Zagreshchenko_7	IGI			README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf 353501_Zagreshchenko_7 
Password:
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd IGI
saneechka@MacBook-Pro-Aleksandr IGI % ls 
saneechka@MacBook-Pro-Aleksandr IGI % git branch
  IGI
* IGI_LR1
  STRWEB
  master
saneechka@MacBook-Pro-Aleksandr IGI % ls 
saneechka@MacBook-Pro-Aleksandr IGI % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rg IGI 
rm: illegal option -- g
usage: rm [-f | -i] [-dIPRrvWx] file ...
       unlink [--] file
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mkdir LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "IGI_LR1 branch"
[IGI_LR1 96c7fcc] IGI_LR1 branch
 2 files changed, 0 insertions(+), 0 deletions(-)
 rename IGI/.gitkeep => .gitkeep (100%)
 delete mode 100644 IGI/LR1/.gitkeep
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 288 байтов | 288.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   e0c7748..96c7fcc  IGI_LR1 -> IGI_LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf .gitkeep
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
  IGI
* IGI_LR1
  STRWEB
  master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf README.md 
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd LR1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
saneechka@MacBook-Pro-Aleksandr LR1 % touch .gitkeep
saneechka@MacBook-Pro-Aleksandr LR1 % ls
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "IGI_LR1 branch"
[IGI_LR1 fb6b4d8] IGI_LR1 branch
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 LR1/.gitkeep
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin         
Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 356 байтов | 356.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   96c7fcc..fb6b4d8  IGI_LR1 -> IGI_LR1
saneechka@MacBook-Pro-Aleksandr LR1 % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls -a
.	..	.git	LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf .gitkeep README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "clear junk"
[IGI_LR1 51bad5f] clear junk
 2 files changed, 1 deletion(-)
 delete mode 100644 .gitkeep
 delete mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (1/1), готово.
Запись объектов: 100% (2/2), 229 байтов | 229.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   fb6b4d8..51bad5f  IGI_LR1 -> IGI_LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI
Переключились на ветку «IGI»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls\
> 
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ks
zsh: command not found: ks
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
IGI		README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf README.md 
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % LS
IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "remove README.md"
[IGI 8534ae1] remove README.md
 1 file changed, 1 deletion(-)
 delete mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (1/1), готово.
Запись объектов: 100% (2/2), 242 байта | 242.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   abdce26..8534ae1  IGI -> IGI
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI_LR
error: pathspec 'IGI_LR' did not match any file(s) known to git
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI_LR1
Переключились на ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI_LR2
Переключились на новую ветку «IGI_LR2»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % rw LR1 LR2
zsh: command not found: rw
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % rn LR1 LR2
zsh: command not found: rn
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR1 LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "create branch2"
[IGI_LR2 37d934b] create branch2
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR1 => LR2}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI_LR2
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (2/2), 233 байта | 233.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'IGI_LR2' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/IGI_LR2
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI_LR2 -> IGI_LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI_LR3
Переключились на новую ветку «IGI_LR3»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR2 LR3
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .   
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "create branch IGI_LR3"
[IGI_LR3 9326ff4] create branch IGI_LR3
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR2 => LR3}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI_LR3              
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (2/2), 240 байтов | 240.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'IGI_LR3' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/IGI_LR3
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI_LR3 -> IGI_LR3
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI_LR4
Переключились на новую ветку «IGI_LR4»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR3 LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "LR4"
[IGI_LR4 667d33c] LR4
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR3 => LR4}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI_LR4
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (2/2), 227 байтов | 227.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'IGI_LR4' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/IGI_LR4
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI_LR4 -> IGI_LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b IGI_LR5
Переключились на новую ветку «IGI_LR5»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR4 LR5
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "create branch IGI_LR5"
[IGI_LR5 bbd7705] create branch IGI_LR5
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR4 => LR5}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI_LR5              
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (2/2), 243 байта | 243.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'IGI_LR5' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/IGI_LR5
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      IGI_LR5 -> IGI_LR5
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout STRWEB
Переключились на ветку «STRWEB»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md	STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf README.md 
Password:
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv STRWEB LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR1 STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b "STRWEB_LR1"
Переключились на новую ветку «STRWEB_LR1»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv STRWEB LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "create branch "
[STRWEB_LR1 07cffb0] create branch
 2 files changed, 1 deletion(-)
 rename {STRWEB => LR1}/.gitkeep (100%)
 delete mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b "STRWEB_LR2"
Переключились на новую ветку «STRWEB_LR2»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR1 LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add . 
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "branch"
[STRWEB_LR2 ac22f92] branch
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR1 => LR2}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (4/4), 425 байтов | 425.00 КиБ/с, готово.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      STRWEB_LR1 -> STRWEB_LR1
 * [new branch]      STRWEB_LR2 -> STRWEB_LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b "STRWEB_LR3"
Переключились на новую ветку «STRWEB_LR3»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR2
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR2 LR3
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR3
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .      
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "branch 3"
[STRWEB_LR3 1bde7ee] branch 3
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR2 => LR3}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout -b "STRWEB_LR4"
Переключились на новую ветку «STRWEB_LR4»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls        
LR3
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR3
usage: mv [-f | -i | -n] [-hv] source target
       mv [-f | -i | -n] [-v] source ... directory
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % mv LR3 LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "branch"
[STRWEB_LR4 3dd8c8f] branch
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename {LR3 => LR4}/.gitkeep (100%)
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (4/4), 420 байтов | 420.00 КиБ/с, готово.
Total 4 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      STRWEB_LR3 -> STRWEB_LR3
 * [new branch]      STRWEB_LR4 -> STRWEB_LR4
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch STRWEB
fatal: a branch named 'STRWEB' already exists
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout STRWEB 
Переключились на ветку «STRWEB»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
README.md	STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf README.md 
Password:
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "delete README.md from branch STRWEB"
[STRWEB da45b45] delete README.md from branch STRWEB
 1 file changed, 1 deletion(-)
 delete mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (1/1), готово.
Запись объектов: 100% (2/2), 259 байтов | 259.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   a9e1dd4..da45b45  STRWEB -> STRWEB
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch -r
  origin/IGI
  origin/IGI_LR1
  origin/IGI_LR2
  origin/IGI_LR3
  origin/IGI_LR4
  origin/IGI_LR5
  origin/STRWEB
  origin/STRWEB_LR1
  origin/STRWEB_LR2
  origin/STRWEB_LR3
  origin/STRWEB_LR4
  origin/master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch -l
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
* STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
* STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI_LR1
Переключились на ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd LR1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
saneechka@MacBook-Pro-Aleksandr LR1 % git clone https://github.com/smartiqaorg/geometric_lib
Клонирование в «geometric_lib»...
remote: Enumerating objects: 35, done.
remote: Total 35 (delta 0), reused 0 (delta 0), pack-reused 35 (from 1)
Получение объектов: 100% (35/35), 4.60 КиБ | 1.53 МиБ/с, готово.
Определение изменений: 100% (6/6), готово.
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
warning: добавление встроенного git репозитория: LR1/geometric_lib
hint: You've added another git repository inside your current repository.
hint: Clones of the outer repository will not contain the contents of
hint: the embedded repository and will not know how to obtain it.
hint: If you meant to add a submodule, use:
hint:
hint: 	git submodule add <url> LR1/geometric_lib
hint:
hint: If you added this path by mistake, you can remove it from the
hint: index with:
hint:
hint: 	git rm --cached LR1/geometric_lib
hint:
hint: See "git help submodule" for more information.
hint: Disable this message with "git config advice.addEmbeddedRepo false"
saneechka@MacBook-Pro-Aleksandr LR1 % ls
geometric_lib
saneechka@MacBook-Pro-Aleksandr LR1 % cd geometric_lib 
saneechka@MacBook-Pro-Aleksandr geometric_lib % ls
circle.py	docs		square.py
saneechka@MacBook-Pro-Aleksandr geometric_lib % nano circle.py 
saneechka@MacBook-Pro-Aleksandr geometric_lib % cd docs
saneechka@MacBook-Pro-Aleksandr docs % ls
README.md
saneechka@MacBook-Pro-Aleksandr docs % nano README.md 
saneechka@MacBook-Pro-Aleksandr docs % cd ..
saneechka@MacBook-Pro-Aleksandr geometric_lib % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % ls
geometric_lib
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "change geometic_lib"
[IGI_LR1 413573c] change geometic_lib
 1 file changed, 1 insertion(+)
 create mode 160000 LR1/geometric_lib
saneechka@MacBook-Pro-Aleksandr LR1 % ls
geometric_lib
saneechka@MacBook-Pro-Aleksandr LR1 % mkdir foo bin foo_1
saneechka@MacBook-Pro-Aleksandr LR1 % nano readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd foo
saneechka@MacBook-Pro-Aleksandr foo % mkdir 425
saneechka@MacBook-Pro-Aleksandr foo % cd 425 
saneechka@MacBook-Pro-Aleksandr 425 % cd ..    
saneechka@MacBook-Pro-Aleksandr foo % ls
425
saneechka@MacBook-Pro-Aleksandr foo % sudo rm -rf 425
Password:
saneechka@MacBook-Pro-Aleksandr foo % ls
saneechka@MacBook-Pro-Aleksandr foo % mkdir 775
saneechka@MacBook-Pro-Aleksandr foo % tree
.
└── 775

2 directories, 0 files
saneechka@MacBook-Pro-Aleksandr foo % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % sudo rm -rf bin
Password:
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd f00
cd: no such file or directory: f00
saneechka@MacBook-Pro-Aleksandr LR1 % cd foo
saneechka@MacBook-Pro-Aleksandr foo % ls
775
saneechka@MacBook-Pro-Aleksandr foo % cd 775
saneechka@MacBook-Pro-Aleksandr 775 % ls
saneechka@MacBook-Pro-Aleksandr 775 % mkdir example
saneechka@MacBook-Pro-Aleksandr 775 % cd example
saneechka@MacBook-Pro-Aleksandr example % ды
zsh: command not found: ды
saneechka@MacBook-Pro-Aleksandr example % ls
saneechka@MacBook-Pro-Aleksandr example % mkdir 775
saneechka@MacBook-Pro-Aleksandr example % cd 775
saneechka@MacBook-Pro-Aleksandr 775 % cd ..
saneechka@MacBook-Pro-Aleksandr example % cd ..
saneechka@MacBook-Pro-Aleksandr 775 % mkdir baz
saneechka@MacBook-Pro-Aleksandr 775 % cd baz
saneechka@MacBook-Pro-Aleksandr baz % mkdir 774
saneechka@MacBook-Pro-Aleksandr baz % cd ..
saneechka@MacBook-Pro-Aleksandr 775 % cd ..
saneechka@MacBook-Pro-Aleksandr foo % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % mkdir bin&cd bin&&mkdir 177&&cd ..
[4] 10788
cd: no such file or directory: bin
saneechka@MacBook-Pro-Aleksandr LR1 % 
[4]    done       mkdir bin
saneechka@MacBook-Pro-Aleksandr LR1 % ls 
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd bin
saneechka@MacBook-Pro-Aleksandr bin % ls 
saneechka@MacBook-Pro-Aleksandr bin % mkdir 177
saneechka@MacBook-Pro-Aleksandr bin % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % ls 
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd foo_1
saneechka@MacBook-Pro-Aleksandr foo_1 % ls
saneechka@MacBook-Pro-Aleksandr foo_1 % mkdir 447
saneechka@MacBook-Pro-Aleksandr foo_1 % cd 447
saneechka@MacBook-Pro-Aleksandr 447 % mkdir grep
saneechka@MacBook-Pro-Aleksandr 447 % cd grep
saneechka@MacBook-Pro-Aleksandr grep % mkdir 547
saneechka@MacBook-Pro-Aleksandr grep % cd ,,
cd: no such file or directory: ,,
saneechka@MacBook-Pro-Aleksandr grep % cd ..
saneechka@MacBook-Pro-Aleksandr 447 % nano test.txt
\%                                                                                                  saneechka@MacBook-Pro-Aleksandr 447 % cd .. 
saneechka@MacBook-Pro-Aleksandr foo_1 % cd .. 
saneechka@MacBook-Pro-Aleksandr LR1 % tree
.
├── bin
│   └── 177
├── foo
│   └── 775
│       ├── baz
│       │   └── 774
│       └── example
│           └── 775
├── foo_1
│   └── 447
│       ├── grep
│       │   └── 547
│       └── test.txt
├── geometric_lib
│   ├── circle.py
│   ├── docs
│   │   └── README.md
│   └── square.py
└── readme.txt

15 directories, 5 files
saneechka@MacBook-Pro-Aleksandr LR1 % cd geometric_lib
saneechka@MacBook-Pro-Aleksandr geometric_lib % ls 
circle.py	docs		square.py
saneechka@MacBook-Pro-Aleksandr geometric_lib % cd docs
saneechka@MacBook-Pro-Aleksandr docs % ls
README.md
saneechka@MacBook-Pro-Aleksandr docs % touch myREADME.md
saneechka@MacBook-Pro-Aleksandr docs % touch test.txt 
saneechka@MacBook-Pro-Aleksandr docs % touch best.txt
saneechka@MacBook-Pro-Aleksandr docs % sudo rm *txt
Password:
saneechka@MacBook-Pro-Aleksandr docs % cd ..  
saneechka@MacBook-Pro-Aleksandr geometric_lib % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git status
Текущая ветка: IGI_LR1
Изменения, которые будут включены в коммит:
  (используйте «git restore --staged <файл>...», чтобы убрать из индекса)
	новый файл:    foo_1/447/test.txt
	новый файл:    readme.txt

Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

saneechka@MacBook-Pro-Aleksandr LR1 % git add . 
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "a-e"
[IGI_LR1 7eb2b31] a-e
 2 files changed, 2 insertions(+)
 create mode 100644 LR1/foo_1/447/test.txt
 create mode 100644 LR1/readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git log
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:50:26 2025 +0300

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:48:44 2025 +0300

    added README
saneechka@MacBook-Pro-Aleksandr LR1 % git log -n 5
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch
saneechka@MacBook-Pro-Aleksandr LR1 % git log --grep="creare"
commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1
saneechka@MacBook-Pro-Aleksandr LR1 % git log --help
\
zsh: suspended  git log --help
saneechka@MacBook-Pro-Aleksandr LR1 % git log --help
saneechka@MacBook-Pro-Aleksandr LR1 % git log -p
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

diff --git a/LR1/foo_1/447/test.txt b/LR1/foo_1/447/test.txt
new file mode 100644
index 0000000..e9b7520
--- /dev/null
+++ b/LR1/foo_1/447/test.txt
@@ -0,0 +1 @@
+447
diff --git a/LR1/readme.txt b/LR1/readme.txt
new file mode 100644
index 0000000..4970e69
--- /dev/null
+++ b/LR1/readme.txt
@@ -0,0 +1 @@
+544

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

diff --git a/LR1/geometric_lib b/LR1/geometric_lib
new file mode 160000
index 0000000..d078c8d
--- /dev/null
+++ b/LR1/geometric_lib
@@ -0,0 +1 @@
+Subproject commit d078c8d9ee6155f3cb0e577d28d337b791de28e2

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

diff --git a/.gitkeep b/.gitkeep
deleted file mode 100644
index e69de29..0000000
diff --git a/README.md b/README.md
deleted file mode 100644
index 9f4e8d7..0000000
--- a/README.md
+++ /dev/null
@@ -1 +0,0 @@
-#test

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

zsh: suspended  git log -p
saneechka@MacBook-Pro-Aleksandr LR1 % git log --relative-date 
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   7 минут назад

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   2 часа назад

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   3 часа назад

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   3 часа назад

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   3 часа назад

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   4 часа назад

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   4 часа назад

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   4 часа назад

    added README
saneechka@MacBook-Pro-Aleksandr LR1 % git log --graph
* commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 17:30:07 2025 +0300
| 
|     a-e
| 
* commit 413573c410cdcce22b9b3e728958682fed64a0bf
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 15:22:16 2025 +0300
| 
|     change geometic_lib
| 
* commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 14:13:16 2025 +0300
| 
|     clear junk
| 
* commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 14:10:49 2025 +0300
| 
|     IGI_LR1 branch
| 
* commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 14:09:16 2025 +0300
| 
|     IGI_LR1 branch
| 
* commit e0c7748ca34189a912e7528617ccdba81faed3d1
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 14:04:07 2025 +0300
| 
|     creare IGI_LR1
| 
* commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
| Author: saneechka <alexandro.dev.work@gmail.com>
| Date:   Thu Feb 20 13:50:26 2025 +0300
| 
|     .gitkeep
| 
* commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
  Author: saneechka <alexandro.dev.work@gmail.com>
  Date:   Thu Feb 20 13:48:44 2025 +0300
  
      added README
saneechka@MacBook-Pro-Aleksandr LR1 % git log -p
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

diff --git a/LR1/foo_1/447/test.txt b/LR1/foo_1/447/test.txt
new file mode 100644
index 0000000..e9b7520
--- /dev/null
+++ b/LR1/foo_1/447/test.txt
@@ -0,0 +1 @@
+447
diff --git a/LR1/readme.txt b/LR1/readme.txt
new file mode 100644
index 0000000..4970e69
--- /dev/null
+++ b/LR1/readme.txt
@@ -0,0 +1 @@
+544

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

diff --git a/LR1/geometric_lib b/LR1/geometric_lib
new file mode 160000
index 0000000..d078c8d
--- /dev/null
+++ b/LR1/geometric_lib
@@ -0,0 +1 @@
+Subproject commit d078c8d9ee6155f3cb0e577d28d337b791de28e2

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

diff --git a/.gitkeep b/.gitkeep
deleted file mode 100644
index e69de29..0000000
diff --git a/README.md b/README.md
deleted file mode 100644
index 9f4e8d7..0000000
--- a/README.md
+++ /dev/null
@@ -1 +0,0 @@

zsh: suspended  git log -p
saneechka@MacBook-Pro-Aleksandr LR1 % git log --stat
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

 LR1/foo_1/447/test.txt | 1 +
 LR1/readme.txt         | 1 +
 2 files changed, 2 insertions(+)

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

 LR1/geometric_lib | 1 +
 1 file changed, 1 insertion(+)

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

 .gitkeep  | 0
 README.md | 1 -
 2 files changed, 1 deletion(-)

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

 LR1/.gitkeep | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

 IGI/.gitkeep => .gitkeep | 0
 IGI/LR1/.gitkeep         | 0
 2 files changed, 0 insertions(+), 0 deletions(-)

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
:



















































commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

 LR1/foo_1/447/test.txt | 1 +
 LR1/readme.txt         | 1 +
 2 files changed, 2 insertions(+)

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

 LR1/geometric_lib | 1 +
 1 file changed, 1 insertion(+)

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

 .gitkeep  | 0
 README.md | 1 -
 2 files changed, 1 deletion(-)

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

 LR1/.gitkeep | 0
 1 file changed, 0 insertions(+), 0 deletions(-)

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

 IGI/.gitkeep => .gitkeep | 0
 IGI/LR1/.gitkeep         | 0
 2 files changed, 0 insertions(+), 0 deletions(-)

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>

zsh: suspended  git log --stat
saneechka@MacBook-Pro-Aleksandr LR1 % git diff --help 

zsh: suspended  git diff --help
saneechka@MacBook-Pro-Aleksandr LR1 % git log
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:50:26 2025 +0300

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:48:44 2025 +0300

    added README
saneechka@MacBook-Pro-Aleksandr LR1 % git diff 413573c410cdcce22b9b3e728958682fed64a0bf 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
diff --git a/LR1/.gitkeep b/.gitkeep
similarity index 100%
rename from LR1/.gitkeep
rename to .gitkeep
diff --git a/LR1/geometric_lib b/LR1/geometric_lib
deleted file mode 160000
index d078c8d..0000000
--- a/LR1/geometric_lib
+++ /dev/null
@@ -1 +0,0 @@
-Subproject commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
diff --git a/README.md b/README.md
new file mode 100644
index 0000000..9f4e8d7
--- /dev/null
+++ b/README.md
@@ -0,0 +1 @@
+#test
saneechka@MacBook-Pro-Aleksandr LR1 % ls 
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % nano test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "before j" 
Текущая ветка: IGI_LR1
Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

индекс пуст (используйте «git add» и/или «git commit -a»)
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -a "before j"
fatal: paths 'before j ...' with -a does not make sense
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "before j"
Текущая ветка: IGI_LR1
Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

индекс пуст (используйте «git add» и/или «git commit -a»)
saneechka@MacBook-Pro-Aleksandr LR1 % git status
Текущая ветка: IGI_LR1
Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

индекс пуст (используйте «git add» и/или «git commit -a»)
saneechka@MacBook-Pro-Aleksandr LR1 % nano test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % ды
zsh: command not found: ды
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	readme.txt	test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add test.txt 
saneechka@MacBook-Pro-Aleksandr LR1 % git status
Текущая ветка: IGI_LR1
Изменения, которые будут включены в коммит:
  (используйте «git restore --staged <файл>...», чтобы убрать из индекса)
	новый файл:    test.txt

Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

saneechka@MacBook-Pro-Aleksandr LR1 % git log    
commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:50:26 2025 +0300

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:48:44 2025 +0300

    added README
saneechka@MacBook-Pro-Aleksandr LR1 % ls        
bin		foo		foo_1		geometric_lib	readme.txt	test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % sudo rm -rf test.txt
Password:
saneechka@MacBook-Pro-Aleksandr LR1 % nano test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "added test.txt"
[IGI_LR1 3da2d2c] added test.txt
 1 file changed, 1 insertion(+)
 create mode 100644 LR1/test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git log  
commit 3da2d2c9debb2e34fd707193fab2e84cd336027b (HEAD -> IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:45:11 2025 +0300

    added test.txt

commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:50:26 2025 +0300

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:48:44 2025 +0300

    added README
(END)

    added test.txt

commit 7eb2b312ba79f4a2ec47c5ff3ee035523b1d932b
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 17:30:07 2025 +0300

    a-e

commit 413573c410cdcce22b9b3e728958682fed64a0bf
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 15:22:16 2025 +0300

    change geometic_lib

commit 51bad5f293fe3b3f436471396a1ddcfa8d41ac56 (origin/IGI_LR1)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:13:16 2025 +0300

    clear junk

commit fb6b4d8ee6f47e1768e67f02aeac2e3e9a170989
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:10:49 2025 +0300

    IGI_LR1 branch

commit 96c7fcc44ca8b09fbdb1c142b1dccf9108eb4940
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:09:16 2025 +0300

    IGI_LR1 branch

commit e0c7748ca34189a912e7528617ccdba81faed3d1
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 14:04:07 2025 +0300

    creare IGI_LR1

commit abdce2673ec52ee8b85354b0e86fcb183f329eb7
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:50:26 2025 +0300

    .gitkeep

commit e34c189d841e7a03bcfa764a4f1ea5e38eacf060 (origin/master, master)
Author: saneechka <alexandro.dev.work@gmail.com>
Date:   Thu Feb 20 13:48:44 2025 +0300

    added README

zsh: suspended  git log
saneechka@MacBook-Pro-Aleksandr LR1 % git revert 3da2d2c9debb2e34fd707193fab2e84cd336027b
error: there was a problem with the editor 'vi'
Пожалуйста, укажите сообщение, при указании опций -m или -F.
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % touch index.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add index.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git reset HEAD index.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout -b newbranch_1
Переключились на новую ветку «newbranch_1»
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	index.txt	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
* newbranch_1
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Перечисление объектов: 16, готово.
Подсчет объектов: 100% (16/16), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (6/6), готово.
Запись объектов: 100% (14/14), 1.04 КиБ | 1.04 МиБ/с, готово.
Total 14 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/saneechka/353501_Zagreshchenko.git
   51bad5f..3da2d2c  IGI_LR1 -> IGI_LR1
 * [new branch]      newbranch_1 -> newbranch_1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo		foo_1		geometric_lib	index.txt	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % nano newbranch1.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "fix"
[newbranch_1 cf029b6] fix
 3 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 LR1/index.txt
 create mode 100644 LR1/newbranch1.txt
 delete mode 100644 LR1/test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Перечисление объектов: 6, готово.
Подсчет объектов: 100% (6/6), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (4/4), 344 байта | 344.00 КиБ/с, готово.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/saneechka/353501_Zagreshchenko.git
   3da2d2c..cf029b6  newbranch_1 -> newbranch_1
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout IGI_LR1
M	LR1/geometric_lib
Переключились на ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr LR1 % git merge newbranch_1
Обновление 3da2d2c..cf029b6
Fast-forward
 LR1/index.txt      | 0
 LR1/newbranch1.txt | 1 +
 LR1/test.txt       | 1 -
 3 files changed, 1 insertion(+), 1 deletion(-)
 create mode 100644 LR1/index.txt
 create mode 100644 LR1/newbranch1.txt
 delete mode 100644 LR1/test.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   3da2d2c..cf029b6  IGI_LR1 -> IGI_LR1
saneechka@MacBook-Pro-Aleksandr LR1 % git branch -d newbranch_1    
Ветка newbranch_1 удалена (была cf029b6).
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout -b new branch
fatal: «branch» не является коммитом, поэтому невозможно создать из него ветку «new»
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout -b newbranch 
Переключились на новую ветку «newbranch»
saneechka@MacBook-Pro-Aleksandr LR1 % whereisi                   
zsh: command not found: whereisi
saneechka@MacBook-Pro-Aleksandr LR1 % whereis 
usage: whereis [-abmqu] [-BM dir ... -f] program ...
saneechka@MacBook-Pro-Aleksandr LR1 % whereis i
i:
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
* newbranch
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout IGI_LR1 -- readme.txt 
saneechka@MacBook-Pro-Aleksandr LR1 % ls
bin		foo_1		index.txt	readme.txt
foo		geometric_lib	newbranch1.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "fix"
Текущая ветка: newbranch
Изменения, которые не в индексе для коммита:
  (используйте «git add <файл>...», чтобы добавить файл в индекс)
  (используйте «git restore <файл>...», чтобы отменить изменения в рабочем каталоге)
  (сделайте коммит или отмените изменения в неотслеживаемом или измененном содержимом в подмодулях)
	изменено:      geometric_lib (изменено содержимое, неотслеживаемое содержимое)

индекс пуст (используйте «git add» и/или «git commit -a»)
saneechka@MacBook-Pro-Aleksandr LR1 % git push origin newbranch      
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'newbranch' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/newbranch
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      newbranch -> newbranch
saneechka@MacBook-Pro-Aleksandr LR1 % sudo rm -rf newbranch1.txt
Password:
saneechka@MacBook-Pro-Aleksandr LR1 % git add .
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "do"
[newbranch f297719] do
 1 file changed, 1 deletion(-)
 delete mode 100644 LR1/newbranch1.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 260 байтов | 260.00 КиБ/с, готово.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/saneechka/353501_Zagreshchenko.git
   cf029b6..f297719  newbranch -> newbranch
saneechka@MacBook-Pro-Aleksandr LR1 % git branch two
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout two
M	LR1/geometric_lib
Переключились на ветку «two»
saneechka@MacBook-Pro-Aleksandr LR1 % touch branch2.txt 
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout newbranch
M	LR1/geometric_lib
Переключились на ветку «newbranch»
saneechka@MacBook-Pro-Aleksandr LR1 % git merge two
Уже актуально.
saneechka@MacBook-Pro-Aleksandr LR1 % git push origin two 
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)

remote: 
remote: Create a pull request for 'two' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/two
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      two -> two
saneechka@MacBook-Pro-Aleksandr LR1 % 
saneechka@MacBook-Pro-Aleksandr LR1 % git branch -d newbranch newbranch_1 two
error: cannot delete branch 'newbranch' used by worktree at '/Users/saneechka/353501_Zagreshchenko_7'
error: branch 'newbranch_1' not found
Ветка two удалена (была f297719).
saneechka@MacBook-Pro-Aleksandr LR1 % git branch -d newbranch  two           
error: cannot delete branch 'newbranch' used by worktree at '/Users/saneechka/353501_Zagreshchenko_7'
error: branch 'two' not found
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
* newbranch
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout master
warning: unable to rmdir 'LR1/geometric_lib': Directory not empty
Переключились на ветку «master»
saneechka@MacBook-Pro-Aleksandr LR1 % git checlout -d newbranch
git: «checlout» не является командой git. Смотрите «git --help».

Самые похожие команды:
	checkout
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout -d newbranch
M	LR1/geometric_lib
HEAD сейчас на f297719 do
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
* (HEAD отделён на refs/heads/newbranch)
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
  newbranch
saneechka@MacBook-Pro-Aleksandr LR1 % git branch -D newbranch
\Ветка newbranch удалена (была f297719).
saneechka@MacBook-Pro-Aleksandr LR1 % \
> 
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
* (HEAD отделён на f297719)
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
saneechka@MacBook-Pro-Aleksandr LR1 % git push --all origin
Everything up-to-date
saneechka@MacBook-Pro-Aleksandr LR1 % git branch -r
  origin/IGI
  origin/IGI_LR1
  origin/IGI_LR2
  origin/IGI_LR3
  origin/IGI_LR4
  origin/IGI_LR5
  origin/STRWEB
  origin/STRWEB_LR1
  origin/STRWEB_LR2
  origin/STRWEB_LR3
  origin/STRWEB_LR4
  origin/master
  origin/newbranch
  origin/newbranch_1
  origin/two
saneechka@MacBook-Pro-Aleksandr LR1 % git push origin --delete newbranch newbranch_1 two
To https://github.com/saneechka/353501_Zagreshchenko.git
 - [deleted]         newbranch
 - [deleted]         newbranch_1
 - [deleted]         two
saneechka@MacBook-Pro-Aleksandr LR1 % git branch two
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout two
M	LR1/geometric_lib
Переключились на ветку «two»
saneechka@MacBook-Pro-Aleksandr LR1 % nano a.txt b.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git checkout master
warning: unable to rmdir 'LR1/geometric_lib': Directory not empty
Переключились на ветку «master»
saneechka@MacBook-Pro-Aleksandr LR1 % git merge two
Обновление e34c189..f297719
Fast-forward
 LR1/.gitkeep           | 0
 LR1/foo_1/447/test.txt | 1 +
 LR1/geometric_lib      | 1 +
 LR1/index.txt          | 0
 LR1/readme.txt         | 1 +
 README.md              | 1 -
 6 files changed, 3 insertions(+), 1 deletion(-)
 create mode 100644 LR1/.gitkeep
 create mode 100644 LR1/foo_1/447/test.txt
 create mode 160000 LR1/geometric_lib
 create mode 100644 LR1/index.txt
 create mode 100644 LR1/readme.txt
 delete mode 100644 README.md
saneechka@MacBook-Pro-Aleksandr LR1 % git push origin master
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 260 байтов | 260.00 КиБ/с, готово.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/saneechka/353501_Zagreshchenko.git
   e34c189..f297719  master -> master
saneechka@MacBook-Pro-Aleksandr LR1 % ls
a.txt		branch2.txt	foo_1		index.txt
bin		foo		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % ls   
a.txt		branch2.txt	foo_1		index.txt
bin		foo		geometric_lib	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % sudo rm -rf LR1
Password:
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "del from master"
[master 823b9a8] del from master
 5 files changed, 3 deletions(-)
 delete mode 100644 LR1/.gitkeep
 delete mode 100644 LR1/foo_1/447/test.txt
 delete mode 160000 LR1/geometric_lib
 delete mode 100644 LR1/index.txt
 delete mode 100644 LR1/readme.txt
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin master         
Перечисление объектов: 3, готово.
Подсчет объектов: 100% (3/3), готово.
Запись объектов: 100% (2/2), 203 байта | 203.00 КиБ/с, готово.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   f297719..823b9a8  master -> master
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout IGI_LR1
Переключились на ветку «IGI_LR1»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd LR1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo_1		geometric_lib	index.txt	newbranch1.txt	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git branch
  IGI
* IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
  two
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo_1		geometric_lib	index.txt	newbranch1.txt	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % cd foo_1
saneechka@MacBook-Pro-Aleksandr foo_1 % ls
447
saneechka@MacBook-Pro-Aleksandr foo_1 % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 %  
saneechka@MacBook-Pro-Aleksandr LR1 % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % cd LR1
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo_1		geometric_lib	index.txt	newbranch1.txt	readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % sudo rm *.txt
saneechka@MacBook-Pro-Aleksandr LR1 % ls
foo_1		geometric_lib
saneechka@MacBook-Pro-Aleksandr LR1 % nano readme.txt
saneechka@MacBook-Pro-Aleksandr LR1 % 
saneechka@MacBook-Pro-Aleksandr LR1 % mkdir bin
saneechka@MacBook-Pro-Aleksandr LR1 % cd bin
saneechka@MacBook-Pro-Aleksandr bin % mkdir 177
saneechka@MacBook-Pro-Aleksandr bin % cd ..
saneechka@MacBook-Pro-Aleksandr LR1 % mkdir foo
saneechka@MacBook-Pro-Aleksandr LR1 % cd foo
saneechka@MacBook-Pro-Aleksandr foo % mkdir 775
saneechka@MacBook-Pro-Aleksandr foo % cd 775
saneechka@MacBook-Pro-Aleksandr 775 % mkdir example baz
saneechka@MacBook-Pro-Aleksandr 775 % cd example 
saneechka@MacBook-Pro-Aleksandr example % mkdir 775
saneechka@MacBook-Pro-Aleksandr example % cd ..
saneechka@MacBook-Pro-Aleksandr 775 % cd baz
saneechka@MacBook-Pro-Aleksandr baz % mkdir 744
saneechka@MacBook-Pro-Aleksandr baz % cd ..
saneechka@MacBook-Pro-Aleksandr 775 % cd ..
saneechka@MacBook-Pro-Aleksandr foo % cd .. 
saneechka@MacBook-Pro-Aleksandr LR1 % git add . 
saneechka@MacBook-Pro-Aleksandr LR1 % git commit -m "fix structure"
[IGI_LR1 0b35223] fix structure
 2 files changed, 1 deletion(-)
 delete mode 100644 LR1/index.txt
 delete mode 100644 LR1/newbranch1.txt
saneechka@MacBook-Pro-Aleksandr LR1 % git push origin IGI/LR1
error: src refspec IGI/LR1 ничему не соответствует
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
saneechka@MacBook-Pro-Aleksandr LR1 % cd ..
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin IGI/LR1      
error: src refspec IGI/LR1 ничему не соответствует
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin  
Перечисление объектов: 5, готово.
Подсчет объектов: 100% (5/5), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 269 байтов | 269.00 КиБ/с, готово.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/saneechka/353501_Zagreshchenko.git
   cf029b6..0b35223  IGI_LR1 -> IGI_LR1
 * [new branch]      two -> two
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch -d two
error: the branch 'two' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D two'
hint: Disable this message with "git config advice.forceDeleteBranch false"
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch -D two
Ветка two удалена (была f297719).
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch two
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % nano TWO.txt
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "two"
[IGI_LR1 c8128a8] two
 1 file changed, 1 insertion(+)
 create mode 100644 TWO.txt
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin two
To https://github.com/saneechka/353501_Zagreshchenko.git
 ! [rejected]        two -> two (non-fast-forward)
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. If you want to integrate the remote changes, use 'git pull'
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout two
Переключились на ветку «two»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % ls
LR1
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push origin two
To https://github.com/saneechka/353501_Zagreshchenko.git
 ! [rejected]        two -> two (non-fast-forward)
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
* two
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git status
Текущая ветка: two
нечего коммитить, нет изменений в рабочем каталоге
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 272 байта | 272.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/saneechka/353501_Zagreshchenko.git
   0b35223..c8128a8  IGI_LR1 -> IGI_LR1
 ! [rejected]        two -> two (non-fast-forward)
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch three
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git checkout three
Переключились на ветку «three»
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % nano three.txt
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % 
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git add .
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git commit -m "three"
[three 528a6d1] three
 1 file changed, 1 insertion(+)
 create mode 100644 three.txt
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --all origin
Перечисление объектов: 4, готово.
Подсчет объектов: 100% (4/4), готово.
При сжатии изменений используется до 8 потоков
Сжатие объектов: 100% (2/2), готово.
Запись объектов: 100% (3/3), 275 байтов | 275.00 КиБ/с, готово.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'three' on GitHub by visiting:
remote:      https://github.com/saneechka/353501_Zagreshchenko/pull/new/three
remote: 
To https://github.com/saneechka/353501_Zagreshchenko.git
 * [new branch]      three -> three
 ! [rejected]        two -> two (non-fast-forward)
error: не удалось отправить некоторые ссылки в «https://github.com/saneechka/353501_Zagreshchenko.git»
hint: Updates were rejected because a pushed branch tip is behind its remote
hint: counterpart. If you want to integrate the remote changes, use 'git pull'
hint: before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push  origin three
Everything up-to-date
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git branch
  IGI
  IGI_LR1
  IGI_LR2
  IGI_LR3
  IGI_LR4
  IGI_LR5
  STRWEB
  STRWEB_LR1
  STRWEB_LR2
  STRWEB_LR3
  STRWEB_LR4
  master
* three
  two
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --delete origin two
To https://github.com/saneechka/353501_Zagreshchenko.git
 - [deleted]         two
saneechka@MacBook-Pro-Aleksandr 353501_Zagreshchenko_7 % git push --delete origin three
To https://github.com/saneechka/353501_Zagreshchenko.git
 - [deleted]         three
