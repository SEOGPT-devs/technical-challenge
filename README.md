# ResumeME!

<p align="center">
  <a
    href="https://github.com/starship/starship/blob/master/docs/pt-BR/guide/README.md"
    ><img
      height="20"
      src="https://raw.githubusercontent.com/starship/starship/master/media/flag-br.png"
      alt="Português do Brasil"
  /></a>
  <a href="https://github.com/starship/starship/blob/master/README.md"
    ><img
      height="20"
      src="https://raw.githubusercontent.com/starship/starship/master/media/flag-us.png"
      alt="English"
  /></a>
</p>

**The minimal and blazing-fast summarization tool for you!**

-   **Wikipedia:** yes, now you can summarize – _the summary!_ 🚀
-   **Github Docs:** shows relevant information at a glance.
-   **News:** Not in the mood to read the news? _Send me the link and I'll make that easier for you._

<a name="🚀-installation"></a>

## 🚀 Installation

### Prerequisites

-   [Python](https://www.python.org/downloads/) installed in version >= `3.12.3`

### Step 1. Download Files

Clone the repository to your system.

Access `.../technical-challenge/` folder.

To verify if you in the right place, list your files and dirs using

```sh
ls
```

You should see something like this.

```
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        12/06/2024     06:19                djangoapp
d-----        11/06/2024     23:38                dotenv_files
d-----        12/06/2024     01:58                scripts
-a----        11/06/2024     20:06            229 .dockerignore
-a----        11/06/2024     20:53           2100 .gitignore
-a----        08/06/2024     20:39              6 .prettierignore
-a----        12/06/2024     02:13            604 docker-compose.yml
-a----        14/06/2024     14:00           1622 Dockerfile
-a----        15/06/2024     19:40           5345 README.md
```

### Step 2. Build the project image

Create a Python Local Environment.

```sh
python -m venv venv .
```

### Step 3. Entering the virtual environment

Activate your venv with

```sh
. venv/Scripts/activate
```

### Step 4. Configure Environment Variables

Are you installing the files because you are testing [pZacca](https://github.com/pZacca)?

<details>
<summary>No</summary>

Create a `.env` file inside `./dotenv_files/`
Based on `.env-example`, fill the new file with your settings and keys.
If you don't have one of those keys, please see [this](#-may-be-useful)

</details>

<details>
<summary>Yes</summary>

Oh, hi there! You can ask me anytime for the MD_API_KEY, it is a HTML to Markdown converter used in the scrapping process.
Or if you wish, click on [here](https://2markdown.com/signup) to create you own, it's free if you make less than 100 API requests per month.

</details>

<details>
<summary>What does 2md do?</summary>

`2markdown` transforms websites into clean Markdown via API, very useful to output formatted summaries. `2md` ntegrates well with [Python-Markdown](https://github.com/Python-Markdown/markdown), that converts `Markdown` files to `HTML` and so allowing perfectly formatted summary outputs.

</details>

In `./dotenv_files/`

### Step 5. Building Docker image

Run this command to build Docker image, it will execute migrations and other commands to build the entire server.

```sh
docker-compose up --build
```

## Step 6. Local Access

Access your `localhost` or `127.0.0.1` in the port `:8000` and have a good use.

## 📚 May be useful

-   [OpenAI API Docs](https://platform.openai.com/docs/api-reference/introduction)
-   [2md API Docs](https://2markdown.com/docs)
-   [Docker Docs](https://docs.docker.com/)
-   [Python Docs](https://docs.python.org/3/)

## 💭 Extras

This project is based on **MVT** (Model - View - Template) architecture. Comparing to **MVC** (Model - View - Controller), MVT takes advantage on beeing easily modificated and loosely coupled. At the same time, project's flow can be harder to understand.

## 🔗 Let's connect!

<p align="left">

<a href="https://linkedin.com/in/pedro-zaccaria/"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>
[![GitHub followers](https://img.shields.io/github/followers/pZacca.svg?style=social&label=Follow)](https://github.com/pZacca?tab=followers)
<a href="https://wa.me/5513997655782"><img alt="Static Badge" src="https://img.shields.io/badge/WhatsApp-grey?logo=whatsapp"></a>

</p>
