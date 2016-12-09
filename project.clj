(defproject cryogen "0.1.0"
            :description "Simple static site generator"
            :url "https://github.com/lacarmen/cryogen"
            :license {:name "Eclipse Public License"
                      :url "http://www.eclipse.org/legal/epl-v10.html"}
            :dependencies [[org.clojure/clojure "1.8.0"]
                           [ring/ring-devel "1.5.0"]
                           [compojure "1.5.1"]
                           [ring-server "0.4.0"]
                           [cryogen-asciidoc "0.1.2"]
                           [cryogen-core "0.1.43"]]
            :plugins [[lein-ring "0.10.0"]]
            :main cryogen.core
            :ring {:init cryogen.server/init
                   :handler cryogen.server/handler})
