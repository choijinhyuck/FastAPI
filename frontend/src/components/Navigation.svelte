<script>
  import { link } from "svelte-spa-router";
  import {
    page,
    keyword,
    access_token,
    username,
    is_login,
  } from "../lib/store";
  import moment from "moment/min/moment-with-locales";
  moment.locale("ko");

  let current = moment().format("LLLL");
  setInterval(() => {
    current = moment().format("LLLL");
  }, 1000);
</script>

<!-- 네비게이션바 -->
<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
  <div class="container-fluid">
    <a
      use:link
      class="navbar-brand"
      href="/"
      on:click={() => {
        ($keyword = ""), ($page = 0);
      }}>Main</a
    >
    <span class="navbar-text"> {current} </span>
    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon" />
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link" href="https://flask.메모.웹.한국/weather">날씨</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://flask.메모.웹.한국/pdf">PDF</a>
        </li>
        {#if $is_login}
          <li class="nav-item">
            <a
              use:link
              href="/user-login"
              class="nav-link"
              on:click={() => {
                $access_token = "";
                $username = "";
                $is_login = false;
              }}>로그아웃 ({$username})</a
            >
          </li>
        {:else}
          <li class="nav-item">
            <a use:link class="nav-link" href="/user-create">회원가입</a>
          </li>
          <li class="nav-item">
            <a use:link class="nav-link" href="/user-login">로그인</a>
          </li>
        {/if}
      </ul>
    </div>
  </div>
</nav>
