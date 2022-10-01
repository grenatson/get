# Здесь собраны подсказки для работы с Git

## Настройка Git
  Чтобы начать работу, нужно ввести данные команды:
  ```
  git config --global user.name "моё имя"
  git config --global user.email "mymail@example.com"
  ```
  Однако на мфти'ишном компьютере что-то не работало, а с чем это может быть связано, я не знаю.
  Возможно, нужно делать локальную настройку:
  ```
  git config user.name "моё имя"
  git config user.email "mymail@example.com"
  ```
  *(по умолчанию настройка по `--local`)*
  
## Работа с SSH-ключами
  ### Проверка на наличие
   `ls -al ~/ssh`[^note]
  ### Создание нового ключа
   `ssh-keygen -t ed25519 -C "mymail@example.com"`
  ### ssh-agent
   'ssh-agent' - программа для хранения и управлением SSH-ключами
   1. `eval "$(ssh-agent -s)"` - запуск программы: *Agent pid **number***
   2. `ssh-add ~/.ssh/key_name` - добавление ключа: *Identity added*
[^note]: ~ - это "user's home directory"

## Репозитории
  ### Клонирование
    `cd your_project`
    `git clone git@github.com:...` - адрес репозитория
  ### Новая ветка
   ```
   git branch
   git checkout -b your-branch-name
   git checkout master
   git brnach -m old-name new-name
   ```
  ### push в ветку
   `git push origin <branch-name>`
  ### Новый репозиторий
   ```
   mkdir new-repo
   cd new-repo
   git init
   ls -a
   ```
  ### "Я куда-то нажал и всё пропало"
   ```
   git log -p full-filename
   git checkout <hash> full-filename
