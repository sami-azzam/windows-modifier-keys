if (process.platform === 'win32' && process.versions.modules) {
  const bindings = require("bindings");
  const modulePath = bindings("control_modifiers");
  module.exports = require(modulePath);
}  else {
    function getModifierState (a){return false};
    function setModifierState (a,b){
        return false
    };
    module.exports = {getModifierState, setModifierState}
}

