<script>
  import ButtonStyleFilled from "../../routes/join/ButtonStyleFilled.svelte";
  import Menu from "./mobile_menu_login.svelte";
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import { tick } from 'svelte';
  

  let showMenu = writable(false);
  let menuRef;

  function toggleMenu() {
    showMenu.update(value => !value);
  }

  function handleClickOutside(event) {
    tick().then(() => {
      if (menuRef && !menuRef.contains(event.target) && !event.target.closest('.hamburger-menu')) {
        showMenu.set(false);
      }
    });
  }

  onMount(() => {
    document.addEventListener('click', handleClickOutside);
    return () => {
      document.removeEventListener('click', handleClickOutside);
    };
  });

  function handleLogout() {
    // 로컬 스토리지에서 'auth_token' 제거
    sessionStorage.removeItem('auth_token');
    alert("로그아웃 되었습니다.");
    goto('/');
  }
</script>

<style>
  .header-container {
    position: fixed; 
    top: 0;
    width: 1200px;
    background: var(--neutral-0, #ffffff);
    padding: 8px 80px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    height: 72px;
    overflow: hidden;
    z-index: 1000; 
    border-style: solid;
    border-color: var(--neutral-2, #dee5ed);
    border-width: 0px 0px 1px 0px;
    width: 1200px;
    align-items: center;
  }

  .brand {
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }

  .brand-link {
    display: flex;
    align-items: center;
  }

  .brand-logo {
    width: 70px;
    height: 70px;
    object-fit: cover;
  }

  .brand-name {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: 'yg-jalnan';
    font-size: 20px;
    line-height: 28px;
    font-weight: 400;
    margin-left: 10px;
  }

  .navigation {
    display: flex;
    flex-direction: row;
    gap: 48px;
    align-items: center;
    justify-content: flex-start;
  }

  .nav-link {
    color: var(--7b95b7, #6b6b6b);
    text-align: center;
    font-family: var(--body-small-font-family, 'DmSans-Regular', sans-serif);
    font-size: var(--body-small-font-size, 24px);
    line-height: var(--body-small-line-height, 24px);
    font-weight: var(--body-small-font-weight, 400);
  }

  .hamburger-menu {
    display: none;
    flex-direction: column;
    gap: 4px;
    cursor: pointer;
  }

  .hamburger-menu.on div:nth-child(1) {
    transform: translateY(7px) rotate(45deg);
  }

  .hamburger-menu.on div:nth-child(2) {
    opacity: 0;
  }

  .hamburger-menu.on div:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
  }

  .hamburger-menu div {
    width: 25px;
    height: 3px;
    background-color: var(--7b95b7, #6b6b6b);
    transition: transform 0.3s;
  }

  .mobile-nav {
    width: 200px;
    display: none;
    flex-direction: column;
    position: fixed;
    top: 72.2px;
    right: 0;
    background-color: var(--neutral-0, #ffffff);
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.08);
    transition: transform 0.3s ease-in-out;
    transform: translateX(100%);
    box-sizing: border-box;
    z-index: 1000;
  }

  .mobile-nav.show {
    transform: translateX(0);
  }

  @media(max-width: 1200px) {
    .header-container {
      padding: 8px 80px;
      width: 100vw;
    }
  }

  @media(max-width: 894px) {
    .header-container {
      padding: 8px 30px;
      width: 100vw;
    }

    .navigation {
      display: none;
    }

    .hamburger-menu {
      display: flex;
    }

    .mobile-nav.show {
      display: flex;
    }
  }

  @media(max-width: 420px) {
    .header-container {
      padding: 8px 16px;
    }

    .brand-name {
      display: none;
    }
  }
  
</style>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&family=Titan+One&display=swap" rel="stylesheet">

  <div class="header-container">
    <div class="brand">
      <a href="/" class="brand-link">
        <img class="brand-logo" src="./logo/logo1.png" alt="logo">
        <div class="brand-name">
          <strong>Make Zenerator</strong>
        </div>
      </a>
    </div>
    <div class="navigation">
      <a href="/aboutus" class="nav-link">About us</a>
      <a href="/" class="nav-link" on:click={handleLogout}>로그아웃</a>
      <ButtonStyleFilled 
        styleVariant="filled"
        style="
          background: var(--6b6b6b, #000000);
          border-color: var(--7b95b7, #6b6b6b);
          flex-shrink: 0;
        " 
        name="생성하기" 
        targetPath="/infogather"
      ></ButtonStyleFilled>
    </div>
    <div class={`hamburger-menu ${$showMenu ? 'on' : ''}`} on:click={toggleMenu}>
      <div></div>
      <div></div>
      <div></div>
    </div>
  </div>
  <div class="mobile-nav" bind:this={menuRef} class:show={$showMenu}>
    <Menu />
  </div>