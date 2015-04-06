package ozymandias

import (
  "io/ioutil"
  "net/http"
)

var (
  staticIndex []byte
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
