// Background
// In modern UI development, especially for complex applications, it's common to structure 
// the interface as a tree of nested components. Each component's visibility can affect 
// the display of its child components. This hierarchical visibility system allows for 
// efficient management of UI states, enabling developers to show or hide entire sections 
// of the interface with minimal code. However, implementing this system correctly can be 
// challenging, particularly when dealing with inherited visibility states.

// Problem
// Your task is to refactor an existing implementation of a component visibility system. 
// The current implementation contains a bug in how components inherit visibility from their ancestors. 
// This bug needs to be addressed through careful refactoring of the Component class.

// Specification
// Each component must have a constructor, specifying:
// - the ID (unique identifier)
// - Child components (array of child components, which may be empty)
// The Visibility property should accept values: true, false, or null.
// The IsVisible property should:
// - Return true if Visibility is true
// - Return false if Visibility is false
// - If Visibility is null:
//   - For the root component, return true
//   - For non-root components, return the value from the nearest ancestor that has a non-null Visibility, 
//     or true if no such component found

// Task
// Refactor the provided Component class to fix the bug in visibility inheritance while maintaining 
// the specified behavior. Your solution should correctly implement the visibility inheritance logic 
// as described in the specification.

// Setup and Validation
// The initial solution setup will be provided in an object-oriented language. The specific syntax 
// and features available will depend on the language used.
// Test cases are available that provide you with both simple and complex UI models.

// Constraints
// - Input is guaranteed to be valid, so focus on the core visibility logic
// - Performance is not a critical concern for this challenge

// Component tree structure limits:
// | Aspect              | Minimum | Maximum |
// |---------------------|---------|---------|
// | Number of components|    1    |   1000  |
// | Tree depth          |    1    |    20   |

// Example
// Consider the following tree structure:

// Root (Visibility: null)
// |-- Child1 (Visibility: true)
// |   |-- Grandchild1 (Visibility: null)
// |   |-- Grandchild2 (Visibility: false)
// |-- Child2 (Visibility: null)
//     |-- Grandchild3 (Visibility: true)

// Expected IsVisible values:
// - Root: true (special case for root when Visibility is null)
// - Child1: true
// - Grandchild1: true (inherits from Child1)
// - Grandchild2: false
// - Child2: true (inherits from Root)
// - Grandchild3: true

// Good luck, and happy refactoring!

// Solution
class Component {
  
  #id;
  #parent;
  #children;
  #visibility;
  
  constructor(id, children) {
    this.#id = id;
    this.#children = children;
    this.#visibility = null;
    this.#parent = null;
    this.#children.forEach(child => child.#parent = this); 
  }
  
  set visibility(value) {
    this.#visibility = value;
  }
  
  locateVisibleAncestor(component){
    // if root
    if(component.#parent===null){
      return component.#visibility !== null ? component.#visibility : true;
    }
    
    if(component.#visibility!==null){
      return component.#visibility;
    } 
    
    // if visibility null recursively locate nearest ancestor with a non null
    return this.locateVisibleAncestor(component.#parent)
  }
  
  get isVisible() {
  
    if (this.#visibility != null) {
      return this.#visibility
    }
    
    return this.locateVisibleAncestor(this)
  }
  
  toString() {
    return this.#id;
  }
}

const { assert } = require("chai");

describe("Playground", function() {
  
  function act(component, expected) {
    const actual = component.isVisible;
    assert.strictEqual(actual, expected, `Component "${component.toString()}" -> isVisible`);
  }
  
  it("Example test #1", function() {
    /*
    Root (Visibility: null)
    |-- Child1 (Visibility: true)
    |   |-- Grandchild1 (Visibility: null)
    |   |-- Grandchild2 (Visibility: false)
    |-- Child2 (Visibility: null)
        |-- Grandchild3 (Visibility: true)
    */
    const grandchild1 = new Component("Grandchild1", []);
    const grandchild2 = new Component("Grandchild2", []);
    const grandchild3 = new Component("Grandchild3", []);
    const child1 = new Component("Child1", [grandchild1, grandchild2]);
    const child2 = new Component("Child2", [grandchild3]);
    const root = new Component("Root", [child1, child2]);
    root.visibility = null;
    child1.visibility = true;
    grandchild1.visibility = null;
    grandchild2.visibility = false;
    child2.visibility = null;
    grandchild3.visibility = true;
    act(root, true);
    act(child1, true);
    act(grandchild1, true);
    act(grandchild2, false);
    act(child2, true);
    act(grandchild3, true);
  });
  
  it("Example test #2", function() {
    /*
    Root (Visibility: false)
    |-- Child1 (Visibility: null)
    |   |-- Grandchild1 (Visibility: null)
    |   |-- Grandchild2 (Visibility: true)
    |-- Child2 (Visibility: null)
        |-- Grandchild3 (Visibility: true)
    */
    const grandchild1 = new Component("Grandchild1", []);
    const grandchild2 = new Component("Grandchild2", []);
    const grandchild3 = new Component("Grandchild3", []);
    const child1 = new Component("Child1", [grandchild1, grandchild2]);
    const child2 = new Component("Child2", [grandchild3]);
    const root = new Component("Root", [child1, child2]);
    root.visibility = false;
    child1.visibility = null;
    grandchild1.visibility = null;
    grandchild2.visibility = true;
    child2.visibility = null;
    grandchild3.visibility = true;
    act(root, false);
    act(child1, false);
    act(grandchild1, false);
    act(grandchild2, true);
    act(child2, false);
    act(grandchild3, true);
  });
});
