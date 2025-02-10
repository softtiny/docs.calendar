// mdBook creates <code> elements with the class 'language-mermaid hljs' whenever you
// define a mermaid code block.
// The mermaid javascript parser looks for elements with a class name 'mermaid'.
// So simply change the class name of the elements to 'mermaid' to make everything work.
function patchMermaidCodeElementClass() {
    var elements = document.getElementsByClassName("language-mermaid");
    Array.from(elements).forEach(element => {
        if (element.tagName.toLowerCase() == "code") {
            element.className = "mermaid";
        }
    });
    
}

patchMermaidCodeElementClass();
mermaid.initialize({
    startOnLoad:true,
    //theme:"forest",
    //look: "classic",
    //look: "handDrawn",
    deterministicIds: false,
    darkMode: true,
    themeVariables:{

        //primaryColor: "#00FF00",
    },
    gantt:{
        deterministicIds: false,
    },
});
