<script>
  let className = "";
  export { className as class };
  export let style;
  export let targetPath = "/";
</script>
<img
  class="placeholder-image {className}"
  style="{style}"
  src={targetPath}
/>

<style>
.placeholder-image {
  border-radius: 24px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  width: 250px;
  height: 250px;
  position: relative;
  overflow: visible;
}
</style>
