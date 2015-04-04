package ozymandias

import (
  //"html/template"
  "io/ioutil"
  "net/http"
)

var (
  staticIndex []byte
  gameTmpl = template.Must(template.ParseFiles("static/game.html"))
)

func init() {
  content, err := ioutil.ReadFile("static/index.html")
  if err != nil {
    panic(err)
  }
  staticIndex = content

  http.HandleFunc("/", root)
}

func root(w http.ResponseWriter, r *http.Request) { w.Write(staticIndex) }

func read(w http.ResponseWriter, r *http.Request) {
  err := gameTmpl.Execute(w, MakeGame())
  if err != nil {
    http.Error(w, err.Error(), http.StatusInternalServerError)
  }
}
