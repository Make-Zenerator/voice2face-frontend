<script>
  let className = "";
  export { className as class };
  export let style;
  export let targetPath = "/join/placeholder-image.svg"
</script>
<img
  class="{'placeholder-image ' + className}"
  style="{'display: flex; flex-direction: row; align-items: center; justify-content: center; flex-shrink: 0; width:100%; height: 100%; object-fit: cover; position: relative; overflow: visible;' + style}"
  src={targetPath}
/>
