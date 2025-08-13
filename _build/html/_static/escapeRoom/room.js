class Room {
    constructor (correctCode, hint, puzzle) {
        this.correctCode = correctCode;
        this.hint = hint;
        this.puzzle = puzzle;
    }

    checkCode (code) {
        return code === this.correctCode;
    }

    getHint () {
        return this.hint;
    }

    getPuzzle () {
        return this.puzzle;
    }

    attemptUnlock (code) {
        if (this.checkCode(code)) {
            this.unlock();
            return true;
        }
        return false;
    }    

    unlock () {
        this.puzzle.unlock();
    }
}