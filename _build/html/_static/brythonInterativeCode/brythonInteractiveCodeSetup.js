class BrythonInteractiveCodeSetup {
    constructor(containerId, initialCode) {
        this.containerId = containerId;
        this.initialCode = initialCode;
        this.uniqueId = this.generateUUID();

        this.editorId = `code-editor-${this.uniqueId}`;
        this.runButtonId = `run-button-${this.uniqueId}`;
        this.resetButtonId = `reset-button-${this.uniqueId}`;
        this.outputId = `output-${this.uniqueId}`;
        this.errorBoxId = `error-box-${this.uniqueId}`;

        this.editorInstance = null;
        this.runnerInstance = null;

        this.createEditorHTML();
        this.setupInteractiveEditor();
    }

    generateUUID() {
        return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
            const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);
            return v.toString(16);
        });
    }

    createEditorHTML() {
        const container = document.getElementById(this.containerId);
        if (!container) {
            console.error(`Container with ID ${this.containerId} not found.`);
            return;
        }

        const html = `
            <div>
                <textarea id="${this.editorId}" name="code-${this.uniqueId}">${this.initialCode}</textarea>
                <button id="${this.runButtonId}" class="button button-run">Run Code</button>
                <button id="${this.resetButtonId}" class="button button-reset">Reset Code</button>
            </div>
            <div id="${this.errorBoxId}"></div>
            <pre id="${this.outputId}" class="pythonoutput"></pre>
        `;

        container.innerHTML = html;
    }

    setupInteractiveEditor() {
        this.editorInstance = new BrythonCodeEditor(this.editorId);
        this.runnerInstance = new BrythonRunner(this.outputId, this.errorBoxId);

        document.getElementById(this.runButtonId).addEventListener("click", () => this.runCode());
        document.getElementById(this.resetButtonId).addEventListener("click", () => this.resetCode());
    }

    runCode() {
        this.clearOutput();
        this.runnerInstance.run(this.editorInstance);
    }

    resetCode() {
        this.clearOutput();
        this.editorInstance.resetEditor(this.initialCode);
    }

    clearOutput() {
        document.getElementById(this.outputId).textContent = "";
        document.getElementById(this.errorBoxId).textContent = "";
    }
}

function makeBrythonInteractiveCode(containerId, initialCode) {
    return new BrythonInteractiveCodeSetup(containerId, initialCode);
}
