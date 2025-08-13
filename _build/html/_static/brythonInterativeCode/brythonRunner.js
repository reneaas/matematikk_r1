class BrythonRunner {
    constructor(outputId, errorBoxId) {
        this.outputId = outputId;
        this.errorBoxId = errorBoxId;
    }

    run(editor) {
        const code = editor.getValue();  // Get the code from the editor
        const scriptId = `brython-script-${Date.now()}`;

        // Clear previous output and errors
        document.getElementById(this.outputId).textContent = "";
        document.getElementById(this.errorBoxId).textContent = "";
        document.getElementById("status-info").innerHTML = "Processing...";

        // Create a script tag to run the Brython code
        const scriptTag = document.createElement('script');
        scriptTag.setAttribute('type', 'text/python');
        scriptTag.id = scriptId;

        // Set up Brython's Turtle properly with set_defaults
        scriptTag.textContent = `
            import sys
            from browser import document, timer
            import turtle

            # Redirect standard output to the output area
            def write(*args):
                document['turtle-print-output'].html += "".join(args)
            sys.stdout.write = write
            sys.stderr.write = write

            # Link Turtle's canvas to the correct div element
            turtle.set_defaults(turtle_canvas_wrapper=document['turtle-div'])
            t = turtle.Turtle()

            try:
                exec("""${code}""")
            except Exception as e:
                document["${this.errorBoxId}"].text = str(e)
            finally:
                turtle.done()

            document['status-info'].html = ''
        `;

        console.log("Successfully ran code.");

        // Append the script tag to the body for execution
        document.body.appendChild(scriptTag);

        // Optionally remove the script after execution to avoid clutter
        setTimeout(() => {
            document.body.removeChild(scriptTag);
        }, 1000);
    }
}
