const util = require('util');

// Data string to be parsed
// var str = '!4m8!1m3!1d1!2d-98.491142!3d29.424349!3m2!1i1024!2i768!4f13.1!7i20!8i20!10b1!12m21!1m1!18b1!2m3!5m1!6e2!20e3!6m12!4b1!23b1!26i1!27i1!41i2!45b1!63m0!67b1!73m0!74i150000!75b1!89b1!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m3!1sEpKSXrysF6S7tgXs-JyIDg%3A22!2zMWk6Mix0OjEyNjk2LGU6MSxwOkVwS1NYcnlzRjZTN3RnWHMtSnlJRGc6MjI!7e81!24m48!1m12!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i768!1m6!1m2!1i974!2i0!2m2!1i1024!2i768!1m6!1m2!1i0!2i0!2m2!1i1024!2i20!1m6!1m2!1i0!2i748!2m2!1i1024!2i768!34m13!2b1!3b1!4b1!6b1!8m3!1b1!3b1!4b1!9b1!12b1!14b1!20b1!23b1!37m1!1e81!42b1!46m1!1e9!47m0!49m1!3b1!50m55!1m54!2m7!1u17!4sSort+by+distance!5e1!9s0ahUKEwiE88KHgOLoAhVCmK0KHY-aCWAQ_KkBCJMIKBc!10m2!17m1!1e2!2m7!1u3!4s!5e1!9s0ahUKEwiE88KHgOLoAhVCmK0KHY-aCWAQ_KkBCJQIKBg!10m2!3m1!1e1!2m7!1u2!4s!5e1!9s0ahUKEwiE88KHgOLoAhVCmK0KHY-aCWAQ_KkBCJUIKBk!10m2!2m1!1e1!2m7!1u1!4s!5e1!9s0ahUKEwiE88KHgOLoAhVCmK0KHY-aCWAQ_KkBCJYIKBo!10m2!1m1!1e1!2m7!1u1!4s!5e1!9s0ahUKEwiE88KHgOLoAhVCmK0KHY-aCWAQ_KkBCJcIKBs!10m2!1m1!1e2!3m6!1u17!2m4!1m2!17m1!1e2!2sDistance!3m1!1u3!3m1!1u2!3m1!1u1!4BIAE!59BQ2dBd0Fn!65m0';
// var str = '!4m12!1m3!1d14477.914214553773!2d-98.49148313480924!3d29.56408458196368!2m3!1f0!2f0!3f0!3m2!1i3440!2i801!4f13.1!7i20!8i0!10b1!12m8!1m1!18b1!2m3!5m1!6e2!20e3!10b1!16b1!19m4!2m3!1i360!2i120!4i8!20m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!22m5!1s8eqZXq3qCc-7tgXXz5SAAw!4m1!2i5600!7e81!12e30!24m48!1m12!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!26m4!2m3!1i80!2i92!4i8!30m28!1m6!1m2!1i0!2i0!2m2!1i458!2i801!1m6!1m2!1i3390!2i0!2m2!1i3440!2i801!1m6!1m2!1i0!2i0!2m2!1i3440!2i20!1m6!1m2!1i0!2i781!2m2!1i3440!2i801!31b1!34m13!2b1!3b1!4b1!6b1!8m3!1b1!3b1!4b1!9b1!12b1!14b1!20b1!23b1!37m1!1e81!42b1!46m1!1e9!47m0!49m1!3b1!50m65!1m60!1m5!1u17!2m3!2m2!17m1!1e2!2m7!1u17!4sSort+by+distance!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMcHKBc!10m2!17m1!1e2!2m7!1u3!4sOpen+now!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMgHKBg!10m2!3m1!1e1!2m7!1u2!4sTop+rated!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMkHKBk!10m2!2m1!1e1!2m7!1u1!4sCheap!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMoHKBo!10m2!1m1!1e1!2m7!1u1!4sUpscale!5e1!9s0ahUKEwjzr-_3gvDoAhUCNKwKHVSKBfUQ_KkBCMsHKBs!10m2!1m1!1e2!3m6!1u17!2m4!1m2!17m1!1e2!2sDistance!3m1!1u3!3m1!1u2!3m1!1u1!4BIAE!2e2!3m2!1b1!3b0!59BQ2dBd0Fn!65m0';
var str= "!1m14!1s1!3m12!1m3!1d1!2d1!3d1!2m3!1f0!2f0!3f0!3m2!1i3440!2i661!4f13.1!12m4!2m3!1i360!2i120!4i8!13m57!2m2!1i203!2i100!3m2!2i4!5b1!6m6!1m2!1i86!2i86!1m2!1i408!2i240!7m42!1m3!1e1!2b0!3e3!1m3!1e2!2b1!3e2!1m3!1e2!2b0!3e3!1m3!1e3!2b0!3e3!1m3!1e8!2b0!3e3!1m3!1e3!2b1!3e2!1m3!1e9!2b1!3e2!1m3!1e10!2b0!3e3!1m3!1e10!2b1!3e2!1m3!1e10!2b0!3e4!2b1!4b1!9b0!14m3!1sEpKSXrysF6S7tgXs-JyIDg!2zMWk6MCx0OjEyNjkwLGU6MTkscjoxLHA6RXBLU1hyeXNGNlM3dGdYcy1KeUlEZzoxMzE!7e81!15m49!1m13!4e1!13m6!2b1!3b1!4b1!6i1!8b1!9b1!18m4!3b1!4b1!5b1!6b1!2b1!5m5!2b1!3b1!5b1!6b1!7b1!10m1!8e3!14m1!3b1!17b1!20m2!1e3!1e6!24b1!25b1!26b1!30m1!2b1!36b1!43b1!52b1!54m1!1b1!55b1!56m2!1b1!3b1!65m5!3m4!1m3!1m2!1i224!2i298!21m28!1m6!1m2!1i0!2i0!2m2!1i458!2i661!1m6!1m2!1i3390!2i0!2m2!1i3440!2i661!1m6!1m2!1i0!2i0!2m2!1i3440!2i20!1m6!1m2!1i0!2i641!2m2!1i3440!2i661!22m1!1e81!29m0!30m1!3b1";
var parts = str.split('!').filter(function(s) { return s.length > 0; }),
    root = [],                      // Root elemet
    curr = root,                    // Current array element being appended to
    m_stack = [root,],              // Stack of "m" elements
    m_count = [parts.length,];      // Number of elements to put under each level

parts.forEach(function(el) {
    var kind = el.substr(1, 1),
        value = el.substr(2);

    // Decrement all the m_counts
    for (var i = 0; i < m_count.length; i++) {
        m_count[i]--;
    }

    if (kind === 'm') {            // Add a new array to capture coming values
        var new_arr = [];
        m_count.push(value);
        curr.push(new_arr);
        m_stack.push(new_arr);
        curr = new_arr;
    }
    else {
        if (kind == 'b') {                                    // Assuming these are boolean
            curr.push(value == '1');
        }
        else if (kind == 'd' || kind == 'f') {                // Float or double
            curr.push(parseFloat(value));
        }
        else if (kind == 'i' || kind == 'u' || kind == 'e') { // Integer, unsigned or enum as int
            curr.push(parseInt(value));
        }
        else {                                                // Store anything else as a string
            curr.push(value);
        }
    }

    // Pop off all the arrays that have their values already
    while (m_count[m_count.length - 1] === 0) {
        m_stack.pop();
        m_count.pop();
        curr = m_stack[m_stack.length - 1];
    }
});

console.log(util.inspect(root, { depth: null }));