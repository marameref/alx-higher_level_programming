# 0x14. Javascript - Web scraping

## Description

Learning Objectives

- Why Javascript programming is amazing (don’t forget to tweet today, with the hashtag #javascriptisamazing :))
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module

## Requirements

- All files are created and executed on Ubuntu 14.04 LTS using Nodejs (version 10)
- All Javascript code is linted with semistandard

## Tasks

<details>
<summary>View Contents</summary>

### [0. Readme](./0-readme.js)

- Write a script that reads and prints the content of a file.
- The first argument is the file path
- The content of the file must be read in utf-8
- If an error occurred during the reading, print the error object

```
guillaume@ubuntu:~/0x14$ ./0-readme.js cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ cat cisfun
C is super fun!
guillaume@ubuntu:~/0x14$ ./0-readme.js doesntexist
{ Error: ENOENT: no such file or directory, open 'doesntexist'
    at Error (native)
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
```

### [1. Write me](./1-writeme.js)

- Write a script that writes a string to a file.
  - The first argument is the file path
  - The second argument is the string to write
  - The content of the file must be written in utf-8
  - If an error occurred during while writing, print the error object


```
guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
```

### [2. Status code](./2-statuscode.js)

- Write a script that display the status code of a GET request.
  - The first argument is the URL to request (GET)
  - The status code must be printed like this: code: <status code>
  - You must use the module request

```
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/status
code: 200
guillaume@ubuntu:~/0x14$ ./2-statuscode.js https://intranet.hbtn.io/doesnt_exist
code: 404
```

### [3. Star wars movie title](./3-starwars_title.js)

- Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
  - The first argument is the episode number
  - You must use the Star wars API with the endpoint http://swapi.co/api/films/:id
  - You must use the module request

```
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 1
A New Hope
guillaume@ubuntu:~/0x14$ ./3-starwars_title.js 5
Attack of the Clones
```

### [4. Star wars Wedge Antilles](./4-starwars_count.js)

- Write a script that prints the number of movies where the character “Wedge Antilles” is present.
  - The first argument is the API URL of the Star wars API: http://swapi.co/api/films/
  - Wedge Antilles is character ID 18
  - You must use the module request

```
guillaume@ubuntu:~/0x14$ ./4-starwars_count.js http://swapi.co/api/films
3
```

### [5. Loripsum](./5-request_store.js)

- Write a script that gets the contents of a webpage and stores it in a file.
  - The first argument is the URL to request
  - The second argument the file path to store the body response
  - The file must be UTF-8 encoded
  - You must use the module request

```
guillaume@ubuntu:~/0x14$ ./5-request_store.js http://loripsum.net/api loripsum
guillaume@ubuntu:~/0x14$ cat loripsum
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Haec quo modo conveniant, non sane intellego. Nam memini etiam quae nolo, oblivisci non possum quae volo. Te enim iudicem aequum puto, modo quae dicat ille bene noris. Terram, mihi crede, ea lanx et maria deprimet. Deinde prima illa, quae in congressu solemus: Quid tu, inquit, huc? Hoc etsi multimodis reprehendi potest, tamen accipio, quod dant. </p>
...
```

### [6. How many completed?](./6-completed_tasks.js)

- Write a script that computes the number of tasks completed by user id.
  - The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
  - You must use the module request

```
guillaume@ubuntu:~/0x14$ ./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos
{ '1': 11,
  '2': 8,
  '3': 7,
  '4': 6,
  '5': 12,
  '6': 6,
  '7': 9,
  '8': 11,
  '9': 8,
  '10': 12 }
```

</details>
