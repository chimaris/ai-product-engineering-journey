| Term                     | Meaning                                                                                                |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **List (`list`)**        | An ordered collection of items. Equivalent to a JavaScript array.                                      |
| **Dictionary (`dict`)**  | A collection of key-value pairs. Equivalent to a JavaScript object.                                    |
| **JSON**                 | JavaScript Object Notation, a common format for exchanging structured data between applications.       |
| **Environment Variable** | A configuration value (such as an API key or database URL) that is stored outside your source code.    |
| **`.env`**               | Stores the actual secret values used by your application. Never commit this file to Git.               |
| **`.env.example`**       | A template showing which environment variables are required, without including the real secret values. |

| Structure | Use when                         |
| --------- | -------------------------------- |
| `list`    | You need an ordered collection   |
| `tuple`   | You need a fixed collection      |
| `set`     | You need unique values           |
| `dict`    | You need key-value relationships |
