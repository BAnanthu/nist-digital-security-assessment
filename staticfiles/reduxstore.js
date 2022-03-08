obj = {}
function counter(state = obj, action) {
    switch (action.type) {
        case 'FUNCTIONS':
            // console.log(action)
            state["Functions"] = action.data
            return state
        case 'DATA':
            // console.log(action)
            state["Data"] = action.data
            return state
        case 'SETTERINDEX':
            // console.log(action)
            state["SetterIndex"] = action.data
            return state
        
        default:
            return state
    }
}

const store = Redux.createStore(counter)