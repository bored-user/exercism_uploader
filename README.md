# exercism_uploader

Simple Python script to submit [Exercism](https://exercism.io) exercises. Just open a track folder (for instance, `[exercism_workspace]/javascript`) and run the script. It'll automatically submit the files to the website. If you need to force the submition (for any reason), just send anything as an `ARGV` argument (`python3 app.py abc`) and it'll force the submition. The script automatically keeps track of the uploaded exercises on `.uploaded` (hidden) file on directory root (so please don't delete it).

As always, feel free to make PRs or open issues. Happy coding!<br>
**P.S.:** You might find [this](https://github.com/bored-user/exercises/tree/master/exercism) interesting!
