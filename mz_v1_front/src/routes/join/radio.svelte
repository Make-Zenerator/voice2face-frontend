<script>
  export let options;
  export let legend;
  export let userSelected;
  export let fontSize = 30;
  export let flexDirection = 'row';
  
  const uniqueID = Math.floor(Math.random() * 100);
  const slugify = (str = "") =>
    str.toLowerCase().replace(/ /g, "-").replace(/\./g, "");
</script>

<div role="radiogroup" 
     class="group-container"
     aria-labelledby={`label-${uniqueID}`}
     style="font-size:{fontSize}px; flex-direction:{flexDirection}" 
     id={`group-${uniqueID}`}>
  <div class="legend" id={`label-${uniqueID}`}>{legend}</div>
  {#each options as { value, label }}
    <input
      class="sr-only"
      type="radio"
      id={slugify(label) + '-' + uniqueID}
      bind:group={userSelected}
      value={value} />
    <label for={slugify(label) + '-' + uniqueID}> {label} </label>
  {/each}
</div>

<style>
  :root {
    --accent-color: CornflowerBlue;
    --gray: #ccc;
  }
  .group-container {
    border-radius: 2px;
    display: flex;
    flex-direction: var(--flexDirection, row);
  }
  .legend {
    font-weight: bold;
  }
  label {
    user-select: none;
    line-height: 1.2em;
    margin-right: 80px;
  }
  .sr-only {
    position: absolute;
    clip: rect(1px, 1px, 1px, 1px);
    padding: 0;
    border: 0;
    height: 1px;
    width: 1px;
    overflow: hidden;
  }
  input[type="radio"] {
    position: absolute;
  }
  input[type="radio"] + label {
    display: block;
    position: relative;
    text-align: left;
  }
  input[type="radio"] + label::before {
    content: "";
    position: relative;
    display: inline-block;
    margin-right: 0.5em;
    width: 1em;
    height: 1em;
    background: transparent;
    border: 1px solid var(--gray, #ccc);
    border-radius: 50%;
    top: 0.2em;
  }
  input[type="radio"]:checked + label::before {
    border: 1px solid var(--gray, #ccc);
    border-radius: 50%;
  }
  input[type="radio"] + label::after {
    content: "";
    position: absolute;
    display: inline-block;
    width: 0.5em;
    height: 0.5em;
    top: 0.45em;
    left: 0.25em;
    background: var(--accent-color, #282828);
    border: 1px solid var(--accent-color, #282828);
    border-radius: 50%;
    transform: scale(0);
  }
  input[type="radio"]:checked + label::after {
    opacity: 1;
    transform: scale(1);
  }
  input[type="radio"]:focus + label::before {
    box-shadow: 0 0 0 1px var(--accent-color, #282828);
    border-radius: 50%;
  }  
  input[type="radio"]:disabled + label {
    color: darken(var(--gray, #ccc), 10);
  }
  input[type="radio"]:disabled + label::before {
    background: var(--gray, #ccc);
  } 
  input[type="radio"] + label::before {
    transition: background 0.3s ease-out;
  }
  input[type="radio"]:checked + label::before {
    transition: background 0.3s ease-in;
  }
  input[type="radio"] + label::after {
    transition: transform 0.2s ease-out;
  }
  input[type="radio"]:checked + label::after {
    transition: transform 0.2s ease-in;
  }
  input[type="radio"]:focus + label::before {
    box-shadow: 0 0px 8px var(--accent-color, #282828);
    border-radius: 50%;
  }
</style>
