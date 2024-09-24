<script>
  export let style;
</script>

<style>
  .menu {
    display: flex;
    flex-direction: column;
    background: #fff;
    width: 100%;
    align-items: center; /* 추가 */
  }
  .menu a {
    color: var(--7b95b7, #6b6b6b);
    padding: 18px 10px;
    width: 100%;
    text-align: center;
    font-family: var(--body-small-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-small-font-size, 24px);
    line-height: var(--body-small-line-height, 18px);
    font-weight: var(--body-small-font-weight, 400);
  }
  .menu a:hover {
    background: #000;
    color: white;
  }
</style>

<div class="menu">
  <a href="/aboutus">About us</a>
  <a href="/login">로그인</a>
  <a href="/join">회원가입</a>
</div>
