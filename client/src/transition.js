// transitions.js
export function typewriter(node, { duration = 50 }) {
    const text = node.textContent;
    const durationPerCharacter = duration / text.length;
    let currentCharacterIndex = 0;
  
    const interval = setInterval(() => {
      if (currentCharacterIndex >= text.length) {
        clearInterval(interval);
      } else {
        node.textContent = text.slice(0, currentCharacterIndex + 1);
        currentCharacterIndex++;
      }
    }, durationPerCharacter);
  
    return {
      destroy() {
        clearInterval(interval);
      }
    };
  }
  