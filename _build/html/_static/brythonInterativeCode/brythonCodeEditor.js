class BrythonCodeEditor {
    constructor(editorId) {
        this.editorId = editorId;
        this.editor = this.initializeEditor(editorId);
        this.setupThemeListener();
    }

    initializeEditor(editorId) {
        return CodeMirror.fromTextArea(document.getElementById(editorId), {
            mode: {
                name: "python",
                version: 3
            },
            lineNumbers: true,
            theme: this.getCurrentTheme(),
            tabSize: 4,
            indentUnit: 4
        });
    }

    getCurrentTheme() {
        const mode = document.documentElement.getAttribute('data-mode');
        return mode === 'dark' ? 'material-darker' : 'default';
    }

    setupThemeListener() {
        const observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.attributeName === 'data-mode') {
                    this.editor.setOption('theme', this.getCurrentTheme());
                }
            });
        });

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['data-mode']
        });

        this.editor.setOption('theme', this.getCurrentTheme());
    }

    setValue(code) {
        this.editor.setValue(code);
    }

    getValue() {
        return this.editor.getValue();
    }

    resetEditor(initialValue = "") {
        this.editor.setValue(initialValue);
    }
}
