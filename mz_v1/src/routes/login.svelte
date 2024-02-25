<script>
    // Svelte script section if needed
    let email;
    
    
  </script>
  
  <header class="site-header">
    <div class="brand-and-navigation">
      <div class="brand-logo">
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/7387e1f2558c4cb68adb47e3cea898b9ad9d6228337bee53a2579a53313abd25?apiKey=6e0b0bf64b4b49c58a8bfeae7e59ace2&" alt="Zenerator Logo" class="logo" />
        <h1 class="brand-name">Make Zenerator</h1>
      </div>
      <nav class="navigation-links">
        <a href="/about-us" class="link">About Us</a>
        <a href="/login" class="link">로그인</a>
        <a href="/join" class="link signup">회원가입</a>
      </nav>
    </div>
  </header>
  <main class="main-content">
    <section class="login-section">
      <div class="login-form-container">
        <form class="login-form">
          <h2 class="form-heading">Login</h2>
          <label for="emailInput" class="visually-hidden" value="email">Email Address</label>
          <input type="email" id="emailInput" class="email-input" placeholder="이메일 입력" aria-label="Email Address" />
          <label for="passwordInput" class="visually-hidden">Password</label>
          <input type="password" id="passwordInput" class="password-input" placeholder="비밀번호 입력" aria-label="Password" />
          <button type="submit" class="login-button">로그인</button>
        </form>
      </div>
      <aside class="login-image">
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/5f3a07ba95aeee7b7dc6c331c93629c80214c09f6ca9e915702fc94d954bb7d8?apiKey=6e0b0bf64b4b49c58a8bfeae7e59ace2&" alt="" class="decorative-image" />
      </aside>
    </section>
  </main>
  <style>
    .site-header {
      background-color: #fff;
      display: flex;
      flex-direction: column;
      border-bottom: 1px solid #dee5ed;
      padding: 9px 80px;
      justify-content: space-between;
    }
    .brand-and-navigation,
    .navigation-links {
      display: flex;
      align-items: center;
      gap: 20px;
    }
    .brand-logo {
      display: flex;
      align-items: end;
    }
    .logo {
      width: 90px;
      object-fit: cover;
    }
    .brand-name {
      margin-left: 10px;
      font-family: 'Titan One', sans-serif;
      font-size: 24px;
    }
    .link {
      text-decoration: none;
      color: #6b6b6b;
      font-size: 16px;
    }
    .signup {
      border-radius: 50px;
      border: 1px solid #6b6b6b;
      background-color: #000;
      color: #fff;
      padding: 12px 18px;
    }
    .main-content {
      display: flex;
      justify-content: center;
      padding: 50px 0;
    }
    .login-section {
      display: flex;
      gap: 20px;
      width: 100%;
      max-width: 1097px;
    }
    .login-form-container,
    .login-image {
      flex: 1;
    }
    .login-form {
      display: flex;
      flex-direction: column;
      gap: 10px;
      border: 0.5px solid #878787;
      padding: 49px 20px;
      box-shadow: 0px 4px 64px 0px rgba(0, 0, 0, 0.05);
      border-radius: 10px;
    }
    .form-heading {
      margin: 0;
      font-size: 46px;
      font-weight: 700;
    }
    .email-input,
    .password-input {
      border-radius: 10px;
      border: 1px solid #000;
      padding: 1px 44px;
    }
    .login-button {
      border-radius: 50px;
      border: 1px solid #486284;
      background-color: #6b6b6b;
      color: #fff;
      padding: 12px 20px;
      cursor: pointer;
    }
    .visually-hidden {
      position: absolute;
      width: 1px;
      height: 1px;
      margin: -1px;
      padding: 0;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border-width: 0;
    }
    .decorative-image {
      max-width: 100%;
      height: auto;
    }
  </style>