





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://assets-cdn.github.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-77c3b874f32e71b14cded5a120f42f5c7288fa52e0a37f2d5919fbd8bcfca63c.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-6518de102c0fb5eefed8021d369596311a18c644778f5d8d1fa7238c4b3870ba.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-71b74cbb2894f6d4629c1a7afffb4692f35cc4213935f1c82967c254daaa14d1.css" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>tensorflow/rnn_cell_impl.py at r1.3 · tensorflow/tensorflow · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars2.githubusercontent.com/u/15658638?v=4&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="tensorflow/tensorflow" property="og:title" /><meta content="https://github.com/tensorflow/tensorflow" property="og:url" /><meta content="tensorflow - Computation using data flow graphs for scalable machine learning" property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="C62C:129F6:18AA9AB:252DE0A:599AC3A4" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="C62C:129F6:18AA9AB:252DE0A:599AC3A4" name="octolytics-dimension-request_id" /><meta content="sea" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="NjUxNjNiZWM3ODVhMTUwMWQxODJhZDg3YTNmOWZjZWJkYWE4OTFkYWJlNzZkZmU3ZDc4N2E4NmViYmM2MWRkYXx7InJlbW90ZV9hZGRyZXNzIjoiMjIyLjE4NS4yMzcuODMiLCJyZXF1ZXN0X2lkIjoiQzYyQzoxMjlGNjoxOEFBOUFCOjI1MkRFMEE6NTk5QUMzQTQiLCJ0aW1lc3RhbXAiOjE1MDMzMTQ4NTMsImhvc3QiOiJnaXRodWIuY29tIn0=">


  <meta name="html-safe-nonce" content="a8c7c4e2c33a743ac9a42584155e795012528de6">

  <meta http-equiv="x-pjax-version" content="f086c7c90a434df01369ca38165e0cd6">
  

      <link href="https://github.com/tensorflow/tensorflow/commits/r1.3.atom" rel="alternate" title="Recent Commits to tensorflow:r1.3" type="application/atom+xml">

  <meta name="description" content="tensorflow - Computation using data flow graphs for scalable machine learning">
  <meta name="go-import" content="github.com/tensorflow/tensorflow git https://github.com/tensorflow/tensorflow.git">

  <meta content="15658638" name="octolytics-dimension-user_id" /><meta content="tensorflow" name="octolytics-dimension-user_login" /><meta content="45717250" name="octolytics-dimension-repository_id" /><meta content="tensorflow/tensorflow" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="45717250" name="octolytics-dimension-repository_network_root_id" /><meta content="tensorflow/tensorflow" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/rnn_cell_impl.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-out env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="px-2 py-4 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        <div class="header header-logged-out position-relative f4 py-3" role="banner">
  <div class="container-lg px-3 clearfix">
    <div class="d-flex flex-justify-between">
      <div class="d-flex">
        <a class="header-logo-invertocat my-0" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
          <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>

        <div class="header-sitemenu clearfix">
            <nav>
              <ul class="d-flex list-style-none">
                  <li class="ml-2">
                    <a href="/features" class="js-selected-navigation-item header-navlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
                      Features
</a>                  </li>
                  <li class="ml-4">
                    <a href="/business" class="js-selected-navigation-item header-navlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
                      Business
</a>                  </li>

                  <li class="ml-4">
                    <a href="/explore" class="js-selected-navigation-item header-navlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
                      Explore
</a>                  </li>

                  <li class="ml-4">
                        <a href="/marketplace" class="js-selected-navigation-item header-navlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:marketplace" data-selected-links=" /marketplace">
                          Marketplace
</a>                  </li>
                  <li class="ml-4">
                    <a href="/pricing" class="js-selected-navigation-item header-navlink px-0 py-2 m-0" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing/developer /pricing/team /pricing/business-hosted /pricing/business-enterprise /pricing">
                      Pricing
</a>                  </li>
              </ul>
            </nav>
        </div>
      </div>

      <div class="d-flex">
          <div class="mt-1 mr-3">
            <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/tensorflow/tensorflow/search" class="js-site-search-form" data-scoped-search-url="/tensorflow/tensorflow/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/rnn_cell_impl.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

          </div>

        <span class="d-inline-block">
            <div class="header-navlink px-0 py-2 m-0">
              <a class="text-bold text-white no-underline" href="/login?return_to=%2Ftensorflow%2Ftensorflow%2Fblob%2Fr1.3%2Ftensorflow%2Fpython%2Fops%2Frnn_cell_impl.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
                <span class="text-gray">or</span>
                <a class="text-bold text-white no-underline" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
            </div>
        </span>
      </div>
    </div>
  </div>
</div>


  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
      



  



    <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
      <div class="container repohead-details-container">

        <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Ftensorflow%2Ftensorflow"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/tensorflow/tensorflow/watchers"
     aria-label="5951 users are watching this repository">
    5,951
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Ftensorflow%2Ftensorflow"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/tensorflow/tensorflow/stargazers"
      aria-label="67421 users starred this repository">
      67,421
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Ftensorflow%2Ftensorflow"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/tensorflow/tensorflow/network" class="social-count"
       aria-label="33071 users forked this repository">
      33,071
    </a>
  </li>
</ul>

        <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/tensorflow" class="url fn" rel="author">tensorflow</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/tensorflow/tensorflow" data-pjax="#js-repo-pjax-container">tensorflow</a></strong>

</h1>

      </div>
      <div class="container">
        
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/tensorflow/tensorflow/tree/r1.3" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /tensorflow/tensorflow/tree/r1.3" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/tensorflow/tensorflow/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /tensorflow/tensorflow/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">980</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/tensorflow/tensorflow/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /tensorflow/tensorflow/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">105</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/tensorflow/tensorflow/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /tensorflow/tensorflow/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


    <div class="reponav-dropdown js-menu-container">
      <button type="button" class="btn-link reponav-item reponav-dropdown js-menu-target " data-no-toggle aria-expanded="false" aria-haspopup="true">
        Insights
        <svg aria-hidden="true" class="octicon octicon-triangle-down v-align-middle text-gray" height="11" version="1.1" viewBox="0 0 12 16" width="8"><path fill-rule="evenodd" d="M0 5l6 6 6-6z"/></svg>
      </button>
      <div class="dropdown-menu-content js-menu-content">
        <div class="dropdown-menu dropdown-menu-sw">
          <a class="dropdown-item" href="/tensorflow/tensorflow/pulse" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
            Pulse
          </a>
          <a class="dropdown-item" href="/tensorflow/tensorflow/graphs" data-skip-pjax>
            <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
            Graphs
          </a>
        </div>
      </div>
    </div>
</nav>

      </div>
    </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
  <a href="/tensorflow/tensorflow/blob/a0bbfa6afec617697576210fb22f3ea9c3a57b61/tensorflow/python/ops/rnn_cell_impl.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:b95c693f387c9c7398f98172e7333b24 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">r1.3</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/0.6.0/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="0.6.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                0.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/SummaryMetadataOptional/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="SummaryMetadataOptional"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                SummaryMetadataOptional
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/andrewharp-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="andrewharp-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                andrewharp-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/aselle-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="aselle-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                aselle-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/chizeng-summaryMetadata/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="chizeng-summaryMetadata"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                chizeng-summaryMetadata
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/code-of-conduct/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="code-of-conduct"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                code-of-conduct
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/dandelionmane-fix-tensorboard-install-master/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="dandelionmane-fix-tensorboard-install-master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dandelionmane-fix-tensorboard-install-master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/dandelionmane-fix-tensorboard-install/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="dandelionmane-fix-tensorboard-install"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                dandelionmane-fix-tensorboard-install
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/fix-doc-doc/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="fix-doc-doc"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix-doc-doc
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/fix_debug_grpc_testlib/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="fix_debug_grpc_testlib"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                fix_debug_grpc_testlib
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/frankchn-add-codeowners/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="frankchn-add-codeowners"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                frankchn-add-codeowners
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/master/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.7/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.7"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.7
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.8/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.8"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.8
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.9/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.9"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.9
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.10/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.10"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.10
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.11/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.11"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.11
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r0.12/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r0.12"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r0.12
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r1.0/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r1.0"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r1.1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r1.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/r1.2/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r1.2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r1.2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/tensorflow/tensorflow/blob/r1.3/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="r1.3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                r1.3
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/remove-tensorboard/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="remove-tensorboard"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                remove-tensorboard
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/revert-10411-branch_157903115/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="revert-10411-branch_157903115"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                revert-10411-branch_157903115
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/summary_metadata/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="summary_metadata"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                summary_metadata
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/tfboyd-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="tfboyd-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                tfboyd-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/vincentvanhoucke-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="vincentvanhoucke-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                vincentvanhoucke-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/vrv-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="vrv-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                vrv-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/yifeif-patch-1/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="yifeif-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                yifeif-patch-1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/yifeif-patch-2/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="yifeif-patch-2"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                yifeif-patch-2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/tensorflow/tensorflow/blob/yifeif-patch-3/tensorflow/python/ops/rnn_cell_impl.py"
               data-name="yifeif-patch-3"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                yifeif-patch-3
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.3.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.3.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0">
                v1.3.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.3.0-rc2/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.3.0-rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0-rc2">
                v1.3.0-rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.3.0-rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.3.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0-rc1">
                v1.3.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.3.0-rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.3.0-rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.3.0-rc0">
                v1.3.0-rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.2.1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.2.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.1">
                v1.2.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.2.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.2.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0">
                v1.2.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.2.0-rc2/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.2.0-rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0-rc2">
                v1.2.0-rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.2.0-rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.2.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0-rc1">
                v1.2.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.2.0-rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.2.0-rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.2.0-rc0">
                v1.2.0-rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.1.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.1.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0">
                v1.1.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.1.0-rc2/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.1.0-rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0-rc2">
                v1.1.0-rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.1.0-rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.1.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0-rc1">
                v1.1.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.1.0-rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.1.0-rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.1.0-rc0">
                v1.1.0-rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.1">
                v1.0.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0">
                v1.0.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.0-rc2/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.0-rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0-rc2">
                v1.0.0-rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.0-rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0-rc1">
                v1.0.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.0-rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.0-rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0-rc0">
                v1.0.0-rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v1.0.0-alpha/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v1.0.0-alpha"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v1.0.0-alpha">
                v1.0.0-alpha
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.12.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.12.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.12.0">
                v0.12.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.11.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.11.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.11.0">
                v0.11.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.11.0rc2/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.11.0rc2"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.11.0rc2">
                v0.11.0rc2
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.11.0rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.11.0rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.11.0rc1">
                v0.11.0rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.11.0rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.11.0rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.11.0rc0">
                v0.11.0rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.10.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.10.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.10.0">
                v0.10.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.10.0rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.10.0rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.10.0rc0">
                v0.10.0rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.9.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.9.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.9.0">
                v0.9.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.9.0rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.9.0rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.9.0rc0">
                v0.9.0rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.8.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.8.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.8.0">
                v0.8.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.8.0rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.8.0rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.8.0rc0">
                v0.8.0rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.7.1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.7.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.7.1">
                v0.7.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.7.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.7.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.7.0">
                v0.7.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/v0.6.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="v0.6.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="v0.6.0">
                v0.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/0.12.1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="0.12.1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.12.1">
                0.12.1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/0.12.0-rc1/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="0.12.0-rc1"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.12.0-rc1">
                0.12.0-rc1
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/0.12.0-rc0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="0.12.0-rc0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.12.0-rc0">
                0.12.0-rc0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/0.6.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="0.6.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.6.0">
                0.6.0
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
              href="/tensorflow/tensorflow/tree/0.5.0/tensorflow/python/ops/rnn_cell_impl.py"
              data-name="0.5.0"
              data-skip-pjax="true"
              rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target" title="0.5.0">
                0.5.0
              </span>
            </a>
        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/tensorflow/tensorflow/find/r1.3"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/tensorflow/tensorflow/tree/r1.3"><span>tensorflow</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a href="/tensorflow/tensorflow/tree/r1.3/tensorflow"><span>tensorflow</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/tensorflow/tensorflow/tree/r1.3/tensorflow/python"><span>python</span></a></span><span class="separator">/</span><span class="js-path-segment"><a href="/tensorflow/tensorflow/tree/r1.3/tensorflow/python/ops"><span>ops</span></a></span><span class="separator">/</span><strong class="final-path">rnn_cell_impl.py</strong>
    </div>
  </div>


  
  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/tensorflow/tensorflow/commit/cf7c008ab150ac8e5edb3ed053d38b2919699796" data-pjax>
          cf7c008
        </a>
        <relative-time datetime="2017-06-28T18:07:44Z">Jun 29, 2017</relative-time>
      </span>
      <div>
        <img alt="@yifeif" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1192265?v=4&amp;s=40" width="20" />
        <a href="/yifeif" class="user-mention" rel="contributor">yifeif</a>
          <a href="/tensorflow/tensorflow/commit/cf7c008ab150ac8e5edb3ed053d38b2919699796" class="message" data-pjax="true" title="Branch 160346151 (#11094)

* Properly handle ops that don't have a CPU kernel

PiperOrigin-RevId: 159655906

* Selected BUILD cleanup in tensorflow/contrib/...

PiperOrigin-RevId: 159673079

* Remove redundant `get` calls on smart pointers

PiperOrigin-RevId: 159675809

* PiperOrigin-RevId: 159698321

* Migrate kernels to boosted_trees.

PiperOrigin-RevId: 159698656

* Fix a bug in the memory optimizer when two inputs to a node are both recomputed

PiperOrigin-RevId: 159700457

* Fixed memory leak that can be triggered by a failed node evaluation

PiperOrigin-RevId: 159707380

* Updates get_started tutorial.

PiperOrigin-RevId: 159709158

* [XLA] Remove unused factory in local_service

PiperOrigin-RevId: 159712806

* Fix typo in docstring

PiperOrigin-RevId: 159714414

* Migrate ops for new version of TensorForest.

PiperOrigin-RevId: 159718610

* Added parameterized tests to reduce window tests.

PiperOrigin-RevId: 159721784

* Use C API to implement Operation.device property

PiperOrigin-RevId: 159723490

* Several Estimator changes:
- support configurable input_fn calling in Estimator subclasses.
- pass params and config to the input_fn.
- allow callables for model_fn and input_fn.

PiperOrigin-RevId: 159725554

* Fixed the scalar output for shard api when outputs_from_all_shards=True.

PiperOrigin-RevId: 159726444

* Automated g4 rollback of changelist 159718610

PiperOrigin-RevId: 159728380

* Adding missing deps to targets in llvm.BUILD. This was only working in non-sandboxed builds.

PiperOrigin-RevId: 159729295

* [XLA:HLO] Move sequence functions from hlo_ordering.h to hlo_scheduling.h.

This is required for upcoming changes to convert the sequence creation functions
(and HeapSimulator and BufferAssignment) over to using the new
Hlo{Dataflow,Alias}Analysis.

It's required because otherwise there's a dependency cycle:

Hlo{Dataflow,Alias}Analysis depends on HloOrdering
CreateMemoryMinimizingSequence will depend on Hlo{Dataflow,Alias}Analysis

There's already a cycle here, if both HloOrdering and
CreateMemoryMinimizingSequence are in the same file.  Also note that:

MinimumMemoryForSequence depends on HeapSimulator
HeapSimulator will depend on Hlo{Dataflow,Alias}Analysis
Hlo{Dataflow,Alias}Analysis depends on HloOrdering

Splitting out the sequence functions resolves the cycle.

Refactoring only; no functional changes.

PiperOrigin-RevId: 159731836

* [XLA:HLO] Split Hlo{Value,Buffer} out of Hlo{Dataflow,Alias}Analysis.

This will make dependencies cleaner for upcoming CLs that will convert
HeapSimulator and HloOrdering to use the new analyses.

No change in functionality.

PiperOrigin-RevId: 159737265

* Internal change

PiperOrigin-RevId: 159738215

* Suggest people need to do some build environment ./configur'ing.

Fixes #4279

PiperOrigin-RevId: 159738412

* Rewrite SameDefinedShape function in ShapeRefiner

PiperOrigin-RevId: 159745894

* [XLA] Remove xla_cpu_*_eigen flags from CPU backends.

These flags are currently de-facto unused; parallelism should be controlled
through the cpu_parallel backend. For configuring Eigen, if needed, the options
should be piped more directly to the code.

PiperOrigin-RevId: 159746509

* Updates layers tutorial and corresponding example.

PiperOrigin-RevId: 159749528

* Further BUILD cleanup

PiperOrigin-RevId: 159749869

* Use more efficient squared_difference

PiperOrigin-RevId: 159751209

* Add log_step_count_steps to RunConfig and allow it to flow to the MonitoredSession.

PiperOrigin-RevId: 159753935

* [XLA] Remove xla_hlo_test_generate_hlo_graph, which is now redundant.

PiperOrigin-RevId: 159755688

* Do not use SSE4.1 instructions on Android builds.

PiperOrigin-RevId: 159756104

* Add nonpublic helper `tf.distributions.util.tridiag` op.

PiperOrigin-RevId: 159757904

* [XLA] Remove dead &quot;in-client&quot; code.
Remove Service::runs_in_client_process_ field and it's dead user. This was
previously used by the &quot;InProcess&quot; methods which have been replaced with
the LocalClient API.

PiperOrigin-RevId: 159759455

* [tf contrib seq2seq] Add monotonic attention mechanisms

* Add monotonic_attention and safe_cumprod helper functions.
* Add _BaseMonotonicAttentionMechanism base class.
* Add BahdanauMonotonicAttention and LuongMonotonicAttention classes.

These attention mechanisms are proposed in
Colin Raffel, Minh-Thang Luong, Peter J. Liu, Ron J. Weiss, Douglas Eck,
&quot;Online and Linear-Time Attention by Enforcing Monotonic Alignments.&quot;
ICML 2017.  https://arxiv.org/abs/1704.00784

PiperOrigin-RevId: 159760073

* Add ability for argmax to output int32 indices.  Default remains int64.

Change is made in a backwards and forward compatible manner, since
we add a new attribute with a default that remains the same, and
simply register a few new kernels.

PiperOrigin-RevId: 159761347

* Automated g4 rollback of changelist 159746509

PiperOrigin-RevId: 159763112

* Raise ValueError if invalid dtype for random_uniform.

PiperOrigin-RevId: 159764956

* Internal change.

PiperOrigin-RevId: 159769520

* Support zero shapes for random_poisson. This matches random_uniform.

PiperOrigin-RevId: 159771215

* Blacklist the quantized ops since they have too many issues (incorrect shape
functions, memory corruptions, ...)

PiperOrigin-RevId: 159772801

* Fixed the shape functions of the QuantizedAdd and QuantizedMul ops

PiperOrigin-RevId: 159772841

* Switch from assigning namedtuple.__new__.__defaults__ to overwriting __new__.

Assigning __defaults__ relies on an implementation detail of CPython, confuses
type checkers (and developers :)), and is error-prone since it doesn't make the
relationship between parameter names and default values explicit.
This CL switches to overloading __new__ instead.

PiperOrigin-RevId: 159773922

* Made sure that we can call the constant folding code twice safely.

PiperOrigin-RevId: 159781607

* Added batch_matmul op dependence to android_extended_ops

PiperOrigin-RevId: 159787178

* Fixes a TODO in head_test.

PiperOrigin-RevId: 159789178

* When configuring per-session thread pools, allow
a pool to be a global pool. This allows a division
between large and small pools, without needing to make
new pool for each session.

PiperOrigin-RevId: 159789678

* Add a multi-head TensorForest estimator.

PiperOrigin-RevId: 159820487

* Have RestoreV2's shape fn set all outputs to unknown shape.

PiperOrigin-RevId: 159835723

* VectorExponential added to distributions.

PiperOrigin-RevId: 159840822

* Fold as many nodes as possible instead of giving up if there is any error.

PiperOrigin-RevId: 159841935

* Removed deprecated summary usage from estimators.
Made name_space usage consistent.

PiperOrigin-RevId: 159846928

* Adding missing license notice to toolchain build files

PiperOrigin-RevId: 159847551

* [XLA] Remove unused flags and move debugging flag to debug options.

PiperOrigin-RevId: 159849759

* Fixes some docstrings in feature_column.

PiperOrigin-RevId: 159850619

* TpuEstimator: Replicate the input_fn to the worker CPU for each shard.

The batch size is configured as follows:
The user may specify a global batch size in their hyperparameters. If the 'batch_size' field is set, then we convert the global batch size into a per-shard batch size by dividing by num_shards before running their input_fn.

PiperOrigin-RevId: 159851773

* Modify beam search decoder to use symbolic shape for vocab size if the static shape is not present.

PiperOrigin-RevId: 159852297

* Generalize cluster initialization to span multiple mini-batches if necessary.

PiperOrigin-RevId: 159852557

* Use a single threaded session for SDCALinearRegressorTest to
avoid incorrect threading test failures (tsan).

PiperOrigin-RevId: 159852818

* Migrate ops for new version of TensorForest.

PiperOrigin-RevId: 159852889

* Replaced constant inputs with variables to ensure most of the graph doesn't get
optimized away

PiperOrigin-RevId: 159853171

* For candidate sampling, add facility to colocate the logit computation with the sharded embeddings.

PiperOrigin-RevId: 159854706

* Added a utility to create parsing spec for regressors (canned estimator)

PiperOrigin-RevId: 159855254

* Fix cuda_kernel_helper_test. std::numeric_limits&lt;int32&gt;::max() doesn't pass, so
I didn't use that.

PiperOrigin-RevId: 159869169

* In tfcompile, prune nodes that are not reachable from the fetches before
building the Graph. This allows loading a graph that contains ops not
needed for the compiled binary.

PiperOrigin-RevId: 159869692

* Fix bugs related to distributions over integers.

- Ensure that the max number of categories does not exceed largest integer-form float.
- Make dtype inference consistent between Categorical and Multinomial
distributions.
- Improve documentation to better reflect that the Categorical
distribution is analogous to `argmax{OneHotCategorical}` (itself being
identical to `argmax{Multinomial(p,n=1)}` but not Multinomial.
- Fix validation_args Heisenberg uncertainty: only validation logic should live under self.validate_args. E.g., validate_args=True would sometimes imply `x=floor(x)` which changes behavior thus making debugging impossible because enabling validation *changes* values.
- Corrected `Geometric` swapping of validate_args` and `allow_nan_stats` default-values.

Fixes #10149

PiperOrigin-RevId: 159872532

* Make HloModule clonable

This CL makes HloModule clonable, which is necessary when we want to run the same compilation twice with the same input.

PiperOrigin-RevId: 159874256

* Internal change.

PiperOrigin-RevId: 159876942

* Implement alternative `monte_carlo.expectation_v2`. This function implements
the reparameterization and score-gradient tricks and does not depend on
tf.Distribution like inputs.

PiperOrigin-RevId: 159877923

* In SE_ASSIGN_OR_RETURN change ConsumeValueOrDie to the preferred std::move ValueOrDie.

PiperOrigin-RevId: 159879754

* If rank is unknown, do not add output shapes to transpose nodes.

PiperOrigin-RevId: 159879840

* Move sparse_fill_empty_rows to new, *significantly* faster, C++ kernel for everyone.

Also fix a bug in the C++ op when the input ST has 0 elements.

PiperOrigin-RevId: 159880044

* Add support of label_keys to DebugClassifier

PiperOrigin-RevId: 159883986

* Register devices under their legacy names

Because some higher level APIs continue to use the legacy name format,
when using ClusterSpec propagation, we need to ensure that we register
the devices under their legacy names as well as their canonical names.

PiperOrigin-RevId: 159885777

* [BatchNorm] Minor fixes to TF doc

PiperOrigin-RevId: 159886125

* Generating TBAA metadata causes the LLVM to miscompile after
https://reviews.llvm.org/rL305938).  Disable TBAA (to stop the miscompiles)
while we fix the root issue.

PiperOrigin-RevId: 159895736

* Improve score-trick to be a valid Csiszar f-Divergence yet numerically stable.

PiperOrigin-RevId: 159896013

* Support advisor in all places (Command line, APIs)
Add expensive operation checker

PiperOrigin-RevId: 159897279

* Added canned estimators to Tensorflow library. List of added estimators:
* DNNClassifier
* DNNRegressor
* LinearClassifer
* LinearRegressor
* DNNLinearCombinedClassifier
* DNNLinearCombinedRegressor

PiperOrigin-RevId: 159898954

* Alligned how model-fns handled params among linear/dnn/combined estimators.

PiperOrigin-RevId: 159899925

* Fixed cmake tests.

PiperOrigin-RevId: 159901417

* [XLA:CPU] Add VLOGs to cpu_compiler.cc

PiperOrigin-RevId: 159902919

* Make occurence (op run times and op definition) selectable
in all views to address the loop problem.

When a node is in loop, its execution times are accumulated, its run times
will increase.

PiperOrigin-RevId: 159912429

* [XLA] Small error message improvement in binop shape inference.

PiperOrigin-RevId: 159920109

* Follow upstream API change from r306058.

PiperOrigin-RevId: 159938416

* [TF:XLA] Update LLVM to upstream revision r306085.

PiperOrigin-RevId: 159946562

* [XLA] Remove unused xla_cpu flag and move another to DebugOptions.

PiperOrigin-RevId: 159952124

* Updates linear.md tutorial

PiperOrigin-RevId: 159956867

* Add TraceMe instrumentation of RunStep in GRPC distributed runtime.
A unique ID is added to each RunStep call that allows the client and server
events to be correlated.

PiperOrigin-RevId: 159956950

* [XLA] Add general F32 implementation for ReducePrecision operation.

This only tests with parameter inputs (which is needed to ensure we actually test on GPUs as well as CPUs); there's no point in separately testing with constants.

PiperOrigin-RevId: 159961430

* Java: NativeLibrary: Fix URL in error message.

And add some detail.
Inspired by #11015

PiperOrigin-RevId: 159962478

* Increase rtol for util_test.

PiperOrigin-RevId: 159971136

* Re-enable IR dumping for the sequential CPU backend.

PiperOrigin-RevId: 159974126

* tfdbg: a few minor fixes and improvements

* Let DumpingDebugWrapperSession and DumpingDebugHook create session_root if it doesn't exist
* Add README.md to tensorflow/python/debug
* Add section &quot;Debugging Keras Models with TFDBG&quot; in debugger.md

PiperOrigin-RevId: 159976070

* Add None check for save_path when restoring checkpoints as if something is wrong in tf.train.latest_checkpoint, it will often return None and it's nice to have a common sense check in restore for this. This way log.error says what has happened.

PiperOrigin-RevId: 159979481

* Don't crash if a metagraph fails to load.

PiperOrigin-RevId: 159981628

* Prepare to not include node_def.proto.h in node_def_util.h

The goal is to make kernels mostly independent of proto headers, which will let
us lock down our .so imports.  This CL makes a bunch of .cc files
either include node_def.proto.h themselves or not need the definition of
NodeDef; a second CL will make node_def_util.h not include node_def.proto.h.

RELNOTES: n/a
PiperOrigin-RevId: 159982117

* Add a few diagnostic flags to help narrow down issues with the LLVM
backends.

PiperOrigin-RevId: 159982441

* Updated wide-n-deep tutorial code to use core version of estimators and feature-columns.

PiperOrigin-RevId: 159984663

* Modify ControlFlowContext to also respect import_scope in 'values_' and keys of 'external_values_'

PiperOrigin-RevId: 159985290

* Add item's graph to partition_graphs in virtual cluster's run method.
Put node op name in timeline_label instead of node_name.

PiperOrigin-RevId: 159986583

* Use short-proto for logging purposes.

A short proto will be output on a single log line, making it
easier for certain automated tools to handle.

PiperOrigin-RevId: 159994005

* Sinh, ArcSinh, Cosh, LogCosh functions added to distributions/python/ops/trig.
Care is taken to ensure a fair bit of stability.

PiperOrigin-RevId: 159995514

* Updates some examples in examples/learn.

PiperOrigin-RevId: 159996397

* Add kernel tests for boosted_trees.

PiperOrigin-RevId: 160002696

* Avoid doing unecessary work in the OptimizeGraph() function whenever possible

PiperOrigin-RevId: 160003173

* Use std::shared_ptr instead of core::RefCounted for Node::Properties

Also changes Node::Properties to a struct and removes underscores from public member variables. This change should make it easier to work with Properties moving forward as the refcount will be automatically updated.

PiperOrigin-RevId: 160003281

* Make the CPU compiler dump optimized IR along with the unoptimized IR.

PiperOrigin-RevId: 160005257

* Disable flaky run_metadata_test.

PiperOrigin-RevId: 160015399

* BUILD cleanup in tensorflow/tools/...

PiperOrigin-RevId: 160018623

* SinhArcSinh bijector added.

This two-parameter diffeomorphism from R --&gt; R allows for skewness and fatter
or thinner tails.  See docstring and also
http://oro.open.ac.uk/22510/1/sinhasinh.pdf

PiperOrigin-RevId: 160019380

* Avoid hardcoded names for temporary files in tests.

These tests (and examples that are run as tests) were using hardcoded names for
temporary files.  This failed when multiple copies of these tests were run in
parallel, or even successively by different users, where the second run could
not overwrite files left by the first.

This change uses the TEST_TMPDIR environment variable used by bazel's test
runner to choose a temporary directory.   If that directory is not set,
/tmp is used, as before.

PiperOrigin-RevId: 160026924

* Fix multinomial doc-string, input arg logits expects to log-probabilities and not log-odds.

PiperOrigin-RevId: 160036709

* Made TensorFlow documentation on LSTMs slightly more accurate.

PiperOrigin-RevId: 160047054

* Follow LLVM/ORC upstream API change in r306166.

PiperOrigin-RevId: 160108102

* Move resampler from sonnet to contrib.

PiperOrigin-RevId: 160134565

* [TPUEstimator] Make input_fn invoked properly with eval on CPU.

PiperOrigin-RevId: 160151890

* Deletes iris_val_based_early_stopping example, which uses deprecated ValidationMonitor.

PiperOrigin-RevId: 160154863

* [XLA] Move HLO dumping flags from service_flags to debug_options_flags

This also removes the duplication in the xla_generate_hlo_graph flag.

This CL also moves the actual dumping logic from Executable to the
hlo_graph_dumper namespace, where it belongs; this is in preparation for
removing the hlo_dumper callback altogether, since it isn't serving any role
beyond what a direct call to hlo_graph_dumper would have (b/62872831 has more
details).

PiperOrigin-RevId: 160154869

* Fix missing variable unref

Direct leak of 56 byte(s) in 1 object(s) allocated from:
    #0 0xf5ee272 in operator new(unsigned long) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf5ee272)
    #1 0x1b51394c in tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*)::'lambda'(tensorflow::Var**)::operator()(tensorflow::Var**) const (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b51394c)
    #2 0x1b5136c0 in std::_Function_handler&lt;tensorflow::Status (tensorflow::Var**), tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*)::'lambda'(tensorflow::Var**)&gt;::_M_invoke(std::_Any_data const&amp;, tensorflow::Var**) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b5136c0)
    #3 0x1b50b289 in std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;::operator()(tensorflow::Var**) const (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50b289)
    #4 0x1b50af88 in tensorflow::Status tensorflow::ResourceMgr::LookupOrCreate&lt;tensorflow::Var&gt;(basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, tensorflow::Var**, std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50af88)
    #5 0x1b50ac10 in tensorflow::Status tensorflow::LookupOrCreateResource&lt;tensorflow::Var&gt;(tensorflow::OpKernelContext*, tensorflow::ResourceHandle const&amp;, tensorflow::Var**, std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50ac10)
    #6 0x1b512f1e in tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b512f1e)
    #7 0x1d1881c7 in tensorflow::ThreadPoolDevice::Compute(tensorflow::OpKernel*, tensorflow::OpKernelContext*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1d1881c7)
    #8 0xf96e0fe in tensorflow::KernelAndDevice::Run(std::vector&lt;tensorflow::Tensor, std::allocator&lt;tensorflow::Tensor&gt; &gt;*, std::vector&lt;tensorflow::Tensor, std::allocator&lt;tensorflow::Tensor&gt; &gt;*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf96e0fe)
    #9 0xf94f9c8 in TFE_Execute (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf94f9c8)
    #10 0xf94356d in TFE_Py_Execute(TFE_Context*, int, char const*, tensorflow::gtl::InlinedVector&lt;TFE_TensorHandle*, 4&gt;*, _object*, tensorflow::gtl::InlinedVector&lt;TFE_TensorHandle*, 2&gt;*, TF_Status*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf94356d)

PiperOrigin-RevId: 160160101

* Simplify strided_slice's shape handling

Now that TensorShape and PartialTensorShape share memory representations, there's no need for an abstract class that makes TensorShape and TensorShapeProto look the same.

RELNOTES: n/a
PiperOrigin-RevId: 160161618

* Added a tool to report the static information that can be extracted from a TF model.

PiperOrigin-RevId: 160162256

* Properly handle RefEnter, RefExit and RefNextIteration nodes.

PiperOrigin-RevId: 160162338

* Switch tfprof to use proto3

PiperOrigin-RevId: 160163483

* Fixes to cuda_config.h.

PiperOrigin-RevId: 160168545

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160171187

* Adds notes to prevent overfitting for Experiment continous_train_and_eval.

PiperOrigin-RevId: 160172692

* Go: Update generated wrapper functions for TensorFlow ops.

PiperOrigin-RevId: 160172985

* Merge changes from github.
END_PUBLIC

Note: this CL will break builds.  cl/159887762 to follow to fix all the breakages.

---
Commit 2336cdf7f authored by Maxwell Paul Brickner&lt;mbrickn@users.noreply.github.com&gt;
Committed by gunan&lt;gunan@google.com&gt;:
Updated link to use HTTPS (#10998)

Howdy!

I just updated a link to use https instead of http.

Thanks!
---
Commit ad0892df1 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] Fixes run_metadata_test for SYCL

 This test is designed to test CUDA specific behavior

---
Commit 6b37a0725 authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Update comments
---
Commit 1699d904a authored by John Lawson&lt;john@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] Fixes CUDA specific test run on SYCL (#56)

The testBadParentValuesOnGPU should only be run on CUDA devices, as the
test checks for particular CUDA behaviour. We don't actually provide a
SYCL kernel for GatherTree and so it's not a problem that the tests
don't target SYCL.
---
Commit 3c1946230 authored by myPrecious&lt;Moriadry@users.noreply.github.com&gt;
Committed by Shanqing Cai&lt;cais@google.com&gt;:
Java API to get the size of specified input list of operations. (#10865)

* Java API to get the size of specified input list of operations

* remove unnecessary explain to avoid bring a new term to users.

---
Commit e911c7480 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] REGISTER -&gt; REGISTER6

---
Commit fbf6c4cec authored by superryanguo&lt;superryanguo@gmail.com&gt;
Committed by superryanguo&lt;superryanguo@gmail.com&gt;:
Simplify the Quickstart section with the weblink is better

---
Commit 72e2918cc authored by Taehoon Lee&lt;taehoonlee@snu.ac.kr&gt;
Committed by Taehoon Lee&lt;taehoonlee@snu.ac.kr&gt;:
Fix typos

---
Commit 90c4406b7 authored by Rishabh Patel&lt;patelrishabh@users.noreply.github.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Correct the learning rate as per the code snippet
---
Commit 03da61134 authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Update ir_array.cc
---
Commit 2df6cd3ac authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Another try
---
Commit af0cbace1 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Transpose to go through Eigen (#10321)

---
Commit fc7361081 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Registers RGBToHSV and HSVToRGB (#91) (#10848)

* [OpenCL] Added RGBToHSV and HSVToRGB

* Aligning '\'
---
Commit 832894ef8 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Registers AdjustContrastv2 (#10949)

* [OpenCL] Registers AdjustContrastv2 (#93)

* [OpenCL] Extended adjust_contrast_op_benchmark_test for OpenCL (#96)

* [OpenCL] Extended adjust_contrast_op_benchmark_test for OpenCL

* simplified to #ifndef

* Changed to &quot;#if GOOGLE_CUDA&quot;

* Update adjust_contrast_op_benchmark_test.cc

* Added comments

---
Commit cb4c2f8d1 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Make TransferBufferToInFeed not virual so it compiles.

---
Commit e89f04d80 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix calling Literal member functions.

---
Commit 15a8df724 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix mac build
clone from meheff's change:
[XLA] Change return type of DeviceAssignment::Deserialize to fix build
breakage on mac.
The mac build had the following error:

error: incomplete type 'xla::DeviceAssignment' used in type trait
expression

This was due to a static method returning a StatusOr&lt;DeviceAssignment&gt;
inside of the definition of DeviceAssignment.

---
Commit a54d43fa4 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Replace LiteralUtil to Literal in compiler/plugin/executor

---
Commit 88a6bb80c authored by Guenther Schmuelling&lt;guschmue@microsoft.com&gt;
Committed by Guenther Schmuelling&lt;guschmue@microsoft.com&gt;:
expand inline for debug builds to limit number of symbols

---
Commit 62fb49d31 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix visibility error for contrib/remote_fused_graph/pylib/BUILD.

---
Commit 4c75252f2 authored by Mark Neumann&lt;markn@allenai.org&gt;
Committed by Mark Neumann&lt;markn@allenai.org&gt;:
fix initial test values to avoid numerical instability

---
Commit b58d98353 authored by sj6077&lt;epik03sj@gmail.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
Fixes of AutoParallel bug (#10368)

* Fix the bug that auto_parallel could replicate variable snapshot name

* Use NodeName in grappler:utils instead of substr, convert variables-&gt;variable_def of grappler item

* remove variable_def from grappler item, exclude snapshot nodes from dont_replicate_nodes in auto_parallel

---
Commit a286b7db8 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Make debug_test slice integer.

---
Commit 97fcfdfa6 authored by Toby Boyd&lt;tobyboyd@google.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Fixed path to seq2seq.py and minor formatting
---
Commit 63c1befb8 authored by Anish Shah&lt;shah.anish07@gmail.com&gt;
Committed by Anish Shah&lt;shah.anish07@gmail.com&gt;:
Improve docs for tf.nn.depthwise_conv2d_native

---
Commit 8d42202b2 authored by Yong Tang&lt;yong.tang.github@outlook.com&gt;
Committed by Yong Tang&lt;yong.tang.github@outlook.com&gt;:
Fix mismatched delete in mkl_tfconv_op.cc

This fix fixes mismatched new[]-delete in mkl_tfconv_op.cc

(the file went through clang-format so there are some additional
changes)

Signed-off-by: Yong Tang &lt;yong.tang.github@outlook.com&gt;

---
Commit 26301bd55 authored by Danny Goodman&lt;goodman.danny@gmail.com&gt;
Committed by Danny Goodman&lt;goodman.danny@gmail.com&gt;:
fix error format

---
Commit b3f33ad46 authored by Yao Zhang&lt;yaozhang@google.com&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Make changes to prepare for the fused option of batch norm to be set to None (None means using fused batch norm if possible).

PiperOrigin-RevId: 159649743

---
Commit a4a469832 authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
[XLA] Add tests for select ops and while loops that produce tuples that contain predicates.

PiperOrigin-RevId: 159645900

---
Commit 980d3f2be authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Use C API to implement Operation.name property

This name property is used in many existing tests including those that
already run with C API enabled (math_ops_test, framework_ops_test,
session_test, session_partial_run_test, math_ops_test_gpu, etc).

PiperOrigin-RevId: 159645767

---
Commit 26239c706 authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Previously we didn't have an implementation of BatchNormInference and BatchNormTraining, which gives a linker error if anyone ever tries to call that. A dummy implementation is friendlier than a linker error.

PiperOrigin-RevId: 159645612

---
Commit f671c5caa authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
BEGIN_PUBLIC
Automated g4 rollback of changelist 159570549

PiperOrigin-RevId: 160182040

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160183349

* Merge changes from github followup.

PiperOrigin-RevId: 160183498

* Automated g4 rollback of changelist 160183498

PiperOrigin-RevId: 160189134

* Automated g4 rollback of changelist 160182040

PiperOrigin-RevId: 160190881

* [XLA] Disallow fuse X into Y if there are paths from X to Y which don't fuse

Just because X can fuse into all of its consumers does not mean that those
consumers can fuse into anything. Depending on the structure of the graph, this
can either result in no performance win at all or, in the case of recurrent
networks, a big performance deficit.

PiperOrigin-RevId: 160194058

* First draft of Tensors segment of the programmer's guide.

PiperOrigin-RevId: 160196550

* First draft of variables unit of programmer's guide.

PiperOrigin-RevId: 160196566

* Make xla::Literal moveable.

PiperOrigin-RevId: 160197273

* Automated g4 rollback of changelist 159897279

PiperOrigin-RevId: 160198598

* Updates text_classification example.

PiperOrigin-RevId: 160200457

* Fix backward compatibility test broken by rollback.

PiperOrigin-RevId: 160222187

* Support advisor in all places (Command line, APIs)
Add expensive operation checker

PiperOrigin-RevId: 160222348

* [XLA] Simplify the fusion heuristic

We had two different aspects of the fusion heuristic:
- Don't fuse a producer into a consumer if there exists a path from the
  producer to the consumer which cannot be fused.
- Don't fuse a producer into a consumer if any consumer of the producer cannot
  fuse.

These can be combined into one, simpler, heuristic.

PiperOrigin-RevId: 160222771

* Automated g4 rollback of changelist 160196566

PiperOrigin-RevId: 160222930

* Automated g4 rollback of changelist 160196550

PiperOrigin-RevId: 160222942

* Lets the HParam parser also accept True and False as inputs, since that's how python prints booleans.

PiperOrigin-RevId: 160234658

* Automated g4 rollback of changelist 155070869

PiperOrigin-RevId: 160249526

* [TF:XLA] Inline the sigmoid operation instead of mapping it elementwise.

PiperOrigin-RevId: 160274436

* Make sure all convolution tests are testing non-trivial cases, i.e. where not all inputs are 0, leading to an all-0 output, which masks most possible bugs.
We do not check-fail on 0-sized dimensions as tests for these special cases
exist.

PiperOrigin-RevId: 160274593

* Explicitly use &quot;dns&quot; URI scheme when using DNS names or literal IP
addresses with gRPC.  This avoids problems in environments in which the
default URI scheme is something other than &quot;dns&quot;.

PiperOrigin-RevId: 160276862

* Add RWSE (root weighted squared error) to the WALS estimator.

PiperOrigin-RevId: 160276937

* Don't include node_def.proto.h in node_def_util.h

The goal is to make kernels mostly independent of proto headers, which will let us lock down our .so imports.

RELNOTES: n/a
PiperOrigin-RevId: 160278032

* [XLA] Add tuple support to Literal::CreateFromShape.

PiperOrigin-RevId: 160278561

* Updates some more examples in examples/learn.

PiperOrigin-RevId: 160278757

* Automated g4 rollback of changelist 160278032

PiperOrigin-RevId: 160280961

* Fixed the bug that Estimator does not make deepcopy of params in constructor

PiperOrigin-RevId: 160281247

* Clean out the config and params in TPUEstimator.

PiperOrigin-RevId: 160281507

* [XLA] Remove the &quot;hlo dumper&quot; parameter of xla::Compiler and its piping.

This dumper is no longer necessary since the restructuring of HLO dumping and
the addition of MaybeDumpHloModule which heeds to the right flags. The
remaining bits didn't have additional functionality, but constituted a lot of
boilerplate that has to be propagated throughout the backends.

PiperOrigin-RevId: 160281798

* [TF:XLA] Refactor the sigmoid op as a rescaled tanh.

PiperOrigin-RevId: 160282472

* Fix uninitialized values in TensorForest code.

PiperOrigin-RevId: 160284420

* [TF:XLA] Update Tensorflow LLVM release to upstream r306370.

Fix broken XLA build.

PiperOrigin-RevId: 160284588

* tfdbg example: fix --tensor_size issue in debug_fibonacci

PiperOrigin-RevId: 160290541

* [SE] ThenConvolveWithAlgorithm vlogs algorithm configs.

PiperOrigin-RevId: 160292762

* Fix documentation of Estimator class (invalid quotes).

PiperOrigin-RevId: 160292803

* Shrink the test size to avoid OOM error on old GPUs.

PiperOrigin-RevId: 160292834

* [TF:XLA] Reject operators with resource outputs on CPU and GPU devices.

We were checking for resource inputs but not resource outputs, which led to accidental fusion of some TensorArray ops on CPU and GPU.

PiperOrigin-RevId: 160294302

* Add a functionality of remote fused graph transformation to fuse graphs by op type

PiperOrigin-RevId: 160300039

* Cudnn compatible LSTMCell and LSTMBlockCell

PiperOrigin-RevId: 160300668

* [XLA] Remove &quot;operand&quot; argument from HandleReducePrecision.

PiperOrigin-RevId: 160301461

* Added more reduce window tests.

PiperOrigin-RevId: 160301509

* Updates more text classification examples in examples/learn.

PiperOrigin-RevId: 160305131

* Use C API to implement Operation._output_types

This change first converts the _output_types member to a property and
then implements it using C API if it is enabled.

PiperOrigin-RevId: 160306227

* Add more tests for BatchNormTraining.
RELNOTES: n/a

PiperOrigin-RevId: 160307959

* Update path to print_selective_registration_header.py in comment

PiperOrigin-RevId: 160308173

* Migrate TensorForest v4 python to contrib.

PiperOrigin-RevId: 160308805

* Automated g4 rollback of changelist 159454657

PiperOrigin-RevId: 160314706

* TESTFIX:  distributions:trig_test wasn't passing in ASAN mode.

PiperOrigin-RevId: 160315597

* tfdbg doc: fixes and improvements

PiperOrigin-RevId: 160318411

* Add a time estimation to HloCostAnalysis and represent properties as a map so that adding more properties will be easier, e.g. in a sub-class.

PiperOrigin-RevId: 160318494

* tfdbg: revert dns:/// prefix in gRPC mode

PiperOrigin-RevId: 160319348

* Moves TensorCApi from c_api.cc to c_api_internal.h, where it can be used
by other code that require access to the underlying TensorBuffers.

PiperOrigin-RevId: 160323362

* Readd the new tensors and variables documents, with tests passing.

PiperOrigin-RevId: 160324191

* Make ResourceHandle not be a proto

I'm trying to make core/kernels independent of protos.  Currently the dtype ResourceHandle is itself a proto.  After this CL, ResourceHandle is a normal C++ type which gets converted to/from ResourceHandleProto at (de)serialization time.

RELNOTES: n/a
PiperOrigin-RevId: 160329002

* Minor cleanup: remove unused dependencies and inclusions

PiperOrigin-RevId: 160334030

* Add name_scopes to mnist_deep.py for a cleaner graph layout.

PiperOrigin-RevId: 160338775

* Add note about `tf.test.mock` to docs for `tf.test`

PiperOrigin-RevId: 160338811

* Internal change.

PiperOrigin-RevId: 160339087

* Fix bugs in ScatterNd and add ScatterNdNonAliasingAdd.

tf.scatter_nd_non_aliasing_add acts similarly to tf.scatter_nd_add but
works on non-ref objects (i.e., Tensors -- not Variables).  This means
it has a gradient with respect to the primary input as well as the
updates.  It does its best to avoid making extra copies of the input.

PiperOrigin-RevId: 160339328

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160340888

* Add checkpoint conversion for models that use the attention mechanism implemented in tensorflow/contrib/legacy_seq2seq/python/ops/seq2seq.py.

PiperOrigin-RevId: 160340994

* Go: Update generated wrapper functions for TensorFlow ops.

PiperOrigin-RevId: 160341769

* Merge changes from github.

PiperOrigin-RevId: 160344052

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160346151

* Load py_test in tensorflow/contrib/boosted_trees/BUILD to fix pip test
visibility failures.

* Disable boosted_trees tests on mac while they are being debugged.">Branch 160346151 (</a><a href="https://github.com/tensorflow/tensorflow/pull/11094" class="issue-link js-issue-link" data-url="https://github.com/tensorflow/tensorflow/issues/11094" data-id="239017638" data-error-text="Failed to load issue title" data-permission-text="Issue title is private">#11094</a><a href="/tensorflow/tensorflow/commit/cf7c008ab150ac8e5edb3ed053d38b2919699796" class="message" data-pjax="true" title="Branch 160346151 (#11094)

* Properly handle ops that don't have a CPU kernel

PiperOrigin-RevId: 159655906

* Selected BUILD cleanup in tensorflow/contrib/...

PiperOrigin-RevId: 159673079

* Remove redundant `get` calls on smart pointers

PiperOrigin-RevId: 159675809

* PiperOrigin-RevId: 159698321

* Migrate kernels to boosted_trees.

PiperOrigin-RevId: 159698656

* Fix a bug in the memory optimizer when two inputs to a node are both recomputed

PiperOrigin-RevId: 159700457

* Fixed memory leak that can be triggered by a failed node evaluation

PiperOrigin-RevId: 159707380

* Updates get_started tutorial.

PiperOrigin-RevId: 159709158

* [XLA] Remove unused factory in local_service

PiperOrigin-RevId: 159712806

* Fix typo in docstring

PiperOrigin-RevId: 159714414

* Migrate ops for new version of TensorForest.

PiperOrigin-RevId: 159718610

* Added parameterized tests to reduce window tests.

PiperOrigin-RevId: 159721784

* Use C API to implement Operation.device property

PiperOrigin-RevId: 159723490

* Several Estimator changes:
- support configurable input_fn calling in Estimator subclasses.
- pass params and config to the input_fn.
- allow callables for model_fn and input_fn.

PiperOrigin-RevId: 159725554

* Fixed the scalar output for shard api when outputs_from_all_shards=True.

PiperOrigin-RevId: 159726444

* Automated g4 rollback of changelist 159718610

PiperOrigin-RevId: 159728380

* Adding missing deps to targets in llvm.BUILD. This was only working in non-sandboxed builds.

PiperOrigin-RevId: 159729295

* [XLA:HLO] Move sequence functions from hlo_ordering.h to hlo_scheduling.h.

This is required for upcoming changes to convert the sequence creation functions
(and HeapSimulator and BufferAssignment) over to using the new
Hlo{Dataflow,Alias}Analysis.

It's required because otherwise there's a dependency cycle:

Hlo{Dataflow,Alias}Analysis depends on HloOrdering
CreateMemoryMinimizingSequence will depend on Hlo{Dataflow,Alias}Analysis

There's already a cycle here, if both HloOrdering and
CreateMemoryMinimizingSequence are in the same file.  Also note that:

MinimumMemoryForSequence depends on HeapSimulator
HeapSimulator will depend on Hlo{Dataflow,Alias}Analysis
Hlo{Dataflow,Alias}Analysis depends on HloOrdering

Splitting out the sequence functions resolves the cycle.

Refactoring only; no functional changes.

PiperOrigin-RevId: 159731836

* [XLA:HLO] Split Hlo{Value,Buffer} out of Hlo{Dataflow,Alias}Analysis.

This will make dependencies cleaner for upcoming CLs that will convert
HeapSimulator and HloOrdering to use the new analyses.

No change in functionality.

PiperOrigin-RevId: 159737265

* Internal change

PiperOrigin-RevId: 159738215

* Suggest people need to do some build environment ./configur'ing.

Fixes #4279

PiperOrigin-RevId: 159738412

* Rewrite SameDefinedShape function in ShapeRefiner

PiperOrigin-RevId: 159745894

* [XLA] Remove xla_cpu_*_eigen flags from CPU backends.

These flags are currently de-facto unused; parallelism should be controlled
through the cpu_parallel backend. For configuring Eigen, if needed, the options
should be piped more directly to the code.

PiperOrigin-RevId: 159746509

* Updates layers tutorial and corresponding example.

PiperOrigin-RevId: 159749528

* Further BUILD cleanup

PiperOrigin-RevId: 159749869

* Use more efficient squared_difference

PiperOrigin-RevId: 159751209

* Add log_step_count_steps to RunConfig and allow it to flow to the MonitoredSession.

PiperOrigin-RevId: 159753935

* [XLA] Remove xla_hlo_test_generate_hlo_graph, which is now redundant.

PiperOrigin-RevId: 159755688

* Do not use SSE4.1 instructions on Android builds.

PiperOrigin-RevId: 159756104

* Add nonpublic helper `tf.distributions.util.tridiag` op.

PiperOrigin-RevId: 159757904

* [XLA] Remove dead &quot;in-client&quot; code.
Remove Service::runs_in_client_process_ field and it's dead user. This was
previously used by the &quot;InProcess&quot; methods which have been replaced with
the LocalClient API.

PiperOrigin-RevId: 159759455

* [tf contrib seq2seq] Add monotonic attention mechanisms

* Add monotonic_attention and safe_cumprod helper functions.
* Add _BaseMonotonicAttentionMechanism base class.
* Add BahdanauMonotonicAttention and LuongMonotonicAttention classes.

These attention mechanisms are proposed in
Colin Raffel, Minh-Thang Luong, Peter J. Liu, Ron J. Weiss, Douglas Eck,
&quot;Online and Linear-Time Attention by Enforcing Monotonic Alignments.&quot;
ICML 2017.  https://arxiv.org/abs/1704.00784

PiperOrigin-RevId: 159760073

* Add ability for argmax to output int32 indices.  Default remains int64.

Change is made in a backwards and forward compatible manner, since
we add a new attribute with a default that remains the same, and
simply register a few new kernels.

PiperOrigin-RevId: 159761347

* Automated g4 rollback of changelist 159746509

PiperOrigin-RevId: 159763112

* Raise ValueError if invalid dtype for random_uniform.

PiperOrigin-RevId: 159764956

* Internal change.

PiperOrigin-RevId: 159769520

* Support zero shapes for random_poisson. This matches random_uniform.

PiperOrigin-RevId: 159771215

* Blacklist the quantized ops since they have too many issues (incorrect shape
functions, memory corruptions, ...)

PiperOrigin-RevId: 159772801

* Fixed the shape functions of the QuantizedAdd and QuantizedMul ops

PiperOrigin-RevId: 159772841

* Switch from assigning namedtuple.__new__.__defaults__ to overwriting __new__.

Assigning __defaults__ relies on an implementation detail of CPython, confuses
type checkers (and developers :)), and is error-prone since it doesn't make the
relationship between parameter names and default values explicit.
This CL switches to overloading __new__ instead.

PiperOrigin-RevId: 159773922

* Made sure that we can call the constant folding code twice safely.

PiperOrigin-RevId: 159781607

* Added batch_matmul op dependence to android_extended_ops

PiperOrigin-RevId: 159787178

* Fixes a TODO in head_test.

PiperOrigin-RevId: 159789178

* When configuring per-session thread pools, allow
a pool to be a global pool. This allows a division
between large and small pools, without needing to make
new pool for each session.

PiperOrigin-RevId: 159789678

* Add a multi-head TensorForest estimator.

PiperOrigin-RevId: 159820487

* Have RestoreV2's shape fn set all outputs to unknown shape.

PiperOrigin-RevId: 159835723

* VectorExponential added to distributions.

PiperOrigin-RevId: 159840822

* Fold as many nodes as possible instead of giving up if there is any error.

PiperOrigin-RevId: 159841935

* Removed deprecated summary usage from estimators.
Made name_space usage consistent.

PiperOrigin-RevId: 159846928

* Adding missing license notice to toolchain build files

PiperOrigin-RevId: 159847551

* [XLA] Remove unused flags and move debugging flag to debug options.

PiperOrigin-RevId: 159849759

* Fixes some docstrings in feature_column.

PiperOrigin-RevId: 159850619

* TpuEstimator: Replicate the input_fn to the worker CPU for each shard.

The batch size is configured as follows:
The user may specify a global batch size in their hyperparameters. If the 'batch_size' field is set, then we convert the global batch size into a per-shard batch size by dividing by num_shards before running their input_fn.

PiperOrigin-RevId: 159851773

* Modify beam search decoder to use symbolic shape for vocab size if the static shape is not present.

PiperOrigin-RevId: 159852297

* Generalize cluster initialization to span multiple mini-batches if necessary.

PiperOrigin-RevId: 159852557

* Use a single threaded session for SDCALinearRegressorTest to
avoid incorrect threading test failures (tsan).

PiperOrigin-RevId: 159852818

* Migrate ops for new version of TensorForest.

PiperOrigin-RevId: 159852889

* Replaced constant inputs with variables to ensure most of the graph doesn't get
optimized away

PiperOrigin-RevId: 159853171

* For candidate sampling, add facility to colocate the logit computation with the sharded embeddings.

PiperOrigin-RevId: 159854706

* Added a utility to create parsing spec for regressors (canned estimator)

PiperOrigin-RevId: 159855254

* Fix cuda_kernel_helper_test. std::numeric_limits&lt;int32&gt;::max() doesn't pass, so
I didn't use that.

PiperOrigin-RevId: 159869169

* In tfcompile, prune nodes that are not reachable from the fetches before
building the Graph. This allows loading a graph that contains ops not
needed for the compiled binary.

PiperOrigin-RevId: 159869692

* Fix bugs related to distributions over integers.

- Ensure that the max number of categories does not exceed largest integer-form float.
- Make dtype inference consistent between Categorical and Multinomial
distributions.
- Improve documentation to better reflect that the Categorical
distribution is analogous to `argmax{OneHotCategorical}` (itself being
identical to `argmax{Multinomial(p,n=1)}` but not Multinomial.
- Fix validation_args Heisenberg uncertainty: only validation logic should live under self.validate_args. E.g., validate_args=True would sometimes imply `x=floor(x)` which changes behavior thus making debugging impossible because enabling validation *changes* values.
- Corrected `Geometric` swapping of validate_args` and `allow_nan_stats` default-values.

Fixes #10149

PiperOrigin-RevId: 159872532

* Make HloModule clonable

This CL makes HloModule clonable, which is necessary when we want to run the same compilation twice with the same input.

PiperOrigin-RevId: 159874256

* Internal change.

PiperOrigin-RevId: 159876942

* Implement alternative `monte_carlo.expectation_v2`. This function implements
the reparameterization and score-gradient tricks and does not depend on
tf.Distribution like inputs.

PiperOrigin-RevId: 159877923

* In SE_ASSIGN_OR_RETURN change ConsumeValueOrDie to the preferred std::move ValueOrDie.

PiperOrigin-RevId: 159879754

* If rank is unknown, do not add output shapes to transpose nodes.

PiperOrigin-RevId: 159879840

* Move sparse_fill_empty_rows to new, *significantly* faster, C++ kernel for everyone.

Also fix a bug in the C++ op when the input ST has 0 elements.

PiperOrigin-RevId: 159880044

* Add support of label_keys to DebugClassifier

PiperOrigin-RevId: 159883986

* Register devices under their legacy names

Because some higher level APIs continue to use the legacy name format,
when using ClusterSpec propagation, we need to ensure that we register
the devices under their legacy names as well as their canonical names.

PiperOrigin-RevId: 159885777

* [BatchNorm] Minor fixes to TF doc

PiperOrigin-RevId: 159886125

* Generating TBAA metadata causes the LLVM to miscompile after
https://reviews.llvm.org/rL305938).  Disable TBAA (to stop the miscompiles)
while we fix the root issue.

PiperOrigin-RevId: 159895736

* Improve score-trick to be a valid Csiszar f-Divergence yet numerically stable.

PiperOrigin-RevId: 159896013

* Support advisor in all places (Command line, APIs)
Add expensive operation checker

PiperOrigin-RevId: 159897279

* Added canned estimators to Tensorflow library. List of added estimators:
* DNNClassifier
* DNNRegressor
* LinearClassifer
* LinearRegressor
* DNNLinearCombinedClassifier
* DNNLinearCombinedRegressor

PiperOrigin-RevId: 159898954

* Alligned how model-fns handled params among linear/dnn/combined estimators.

PiperOrigin-RevId: 159899925

* Fixed cmake tests.

PiperOrigin-RevId: 159901417

* [XLA:CPU] Add VLOGs to cpu_compiler.cc

PiperOrigin-RevId: 159902919

* Make occurence (op run times and op definition) selectable
in all views to address the loop problem.

When a node is in loop, its execution times are accumulated, its run times
will increase.

PiperOrigin-RevId: 159912429

* [XLA] Small error message improvement in binop shape inference.

PiperOrigin-RevId: 159920109

* Follow upstream API change from r306058.

PiperOrigin-RevId: 159938416

* [TF:XLA] Update LLVM to upstream revision r306085.

PiperOrigin-RevId: 159946562

* [XLA] Remove unused xla_cpu flag and move another to DebugOptions.

PiperOrigin-RevId: 159952124

* Updates linear.md tutorial

PiperOrigin-RevId: 159956867

* Add TraceMe instrumentation of RunStep in GRPC distributed runtime.
A unique ID is added to each RunStep call that allows the client and server
events to be correlated.

PiperOrigin-RevId: 159956950

* [XLA] Add general F32 implementation for ReducePrecision operation.

This only tests with parameter inputs (which is needed to ensure we actually test on GPUs as well as CPUs); there's no point in separately testing with constants.

PiperOrigin-RevId: 159961430

* Java: NativeLibrary: Fix URL in error message.

And add some detail.
Inspired by #11015

PiperOrigin-RevId: 159962478

* Increase rtol for util_test.

PiperOrigin-RevId: 159971136

* Re-enable IR dumping for the sequential CPU backend.

PiperOrigin-RevId: 159974126

* tfdbg: a few minor fixes and improvements

* Let DumpingDebugWrapperSession and DumpingDebugHook create session_root if it doesn't exist
* Add README.md to tensorflow/python/debug
* Add section &quot;Debugging Keras Models with TFDBG&quot; in debugger.md

PiperOrigin-RevId: 159976070

* Add None check for save_path when restoring checkpoints as if something is wrong in tf.train.latest_checkpoint, it will often return None and it's nice to have a common sense check in restore for this. This way log.error says what has happened.

PiperOrigin-RevId: 159979481

* Don't crash if a metagraph fails to load.

PiperOrigin-RevId: 159981628

* Prepare to not include node_def.proto.h in node_def_util.h

The goal is to make kernels mostly independent of proto headers, which will let
us lock down our .so imports.  This CL makes a bunch of .cc files
either include node_def.proto.h themselves or not need the definition of
NodeDef; a second CL will make node_def_util.h not include node_def.proto.h.

RELNOTES: n/a
PiperOrigin-RevId: 159982117

* Add a few diagnostic flags to help narrow down issues with the LLVM
backends.

PiperOrigin-RevId: 159982441

* Updated wide-n-deep tutorial code to use core version of estimators and feature-columns.

PiperOrigin-RevId: 159984663

* Modify ControlFlowContext to also respect import_scope in 'values_' and keys of 'external_values_'

PiperOrigin-RevId: 159985290

* Add item's graph to partition_graphs in virtual cluster's run method.
Put node op name in timeline_label instead of node_name.

PiperOrigin-RevId: 159986583

* Use short-proto for logging purposes.

A short proto will be output on a single log line, making it
easier for certain automated tools to handle.

PiperOrigin-RevId: 159994005

* Sinh, ArcSinh, Cosh, LogCosh functions added to distributions/python/ops/trig.
Care is taken to ensure a fair bit of stability.

PiperOrigin-RevId: 159995514

* Updates some examples in examples/learn.

PiperOrigin-RevId: 159996397

* Add kernel tests for boosted_trees.

PiperOrigin-RevId: 160002696

* Avoid doing unecessary work in the OptimizeGraph() function whenever possible

PiperOrigin-RevId: 160003173

* Use std::shared_ptr instead of core::RefCounted for Node::Properties

Also changes Node::Properties to a struct and removes underscores from public member variables. This change should make it easier to work with Properties moving forward as the refcount will be automatically updated.

PiperOrigin-RevId: 160003281

* Make the CPU compiler dump optimized IR along with the unoptimized IR.

PiperOrigin-RevId: 160005257

* Disable flaky run_metadata_test.

PiperOrigin-RevId: 160015399

* BUILD cleanup in tensorflow/tools/...

PiperOrigin-RevId: 160018623

* SinhArcSinh bijector added.

This two-parameter diffeomorphism from R --&gt; R allows for skewness and fatter
or thinner tails.  See docstring and also
http://oro.open.ac.uk/22510/1/sinhasinh.pdf

PiperOrigin-RevId: 160019380

* Avoid hardcoded names for temporary files in tests.

These tests (and examples that are run as tests) were using hardcoded names for
temporary files.  This failed when multiple copies of these tests were run in
parallel, or even successively by different users, where the second run could
not overwrite files left by the first.

This change uses the TEST_TMPDIR environment variable used by bazel's test
runner to choose a temporary directory.   If that directory is not set,
/tmp is used, as before.

PiperOrigin-RevId: 160026924

* Fix multinomial doc-string, input arg logits expects to log-probabilities and not log-odds.

PiperOrigin-RevId: 160036709

* Made TensorFlow documentation on LSTMs slightly more accurate.

PiperOrigin-RevId: 160047054

* Follow LLVM/ORC upstream API change in r306166.

PiperOrigin-RevId: 160108102

* Move resampler from sonnet to contrib.

PiperOrigin-RevId: 160134565

* [TPUEstimator] Make input_fn invoked properly with eval on CPU.

PiperOrigin-RevId: 160151890

* Deletes iris_val_based_early_stopping example, which uses deprecated ValidationMonitor.

PiperOrigin-RevId: 160154863

* [XLA] Move HLO dumping flags from service_flags to debug_options_flags

This also removes the duplication in the xla_generate_hlo_graph flag.

This CL also moves the actual dumping logic from Executable to the
hlo_graph_dumper namespace, where it belongs; this is in preparation for
removing the hlo_dumper callback altogether, since it isn't serving any role
beyond what a direct call to hlo_graph_dumper would have (b/62872831 has more
details).

PiperOrigin-RevId: 160154869

* Fix missing variable unref

Direct leak of 56 byte(s) in 1 object(s) allocated from:
    #0 0xf5ee272 in operator new(unsigned long) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf5ee272)
    #1 0x1b51394c in tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*)::'lambda'(tensorflow::Var**)::operator()(tensorflow::Var**) const (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b51394c)
    #2 0x1b5136c0 in std::_Function_handler&lt;tensorflow::Status (tensorflow::Var**), tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*)::'lambda'(tensorflow::Var**)&gt;::_M_invoke(std::_Any_data const&amp;, tensorflow::Var**) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b5136c0)
    #3 0x1b50b289 in std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;::operator()(tensorflow::Var**) const (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50b289)
    #4 0x1b50af88 in tensorflow::Status tensorflow::ResourceMgr::LookupOrCreate&lt;tensorflow::Var&gt;(basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, basic_string&lt;char, std::char_traits&lt;char&gt;, std::allocator&lt;char&gt; &gt; const&amp;, tensorflow::Var**, std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50af88)
    #5 0x1b50ac10 in tensorflow::Status tensorflow::LookupOrCreateResource&lt;tensorflow::Var&gt;(tensorflow::OpKernelContext*, tensorflow::ResourceHandle const&amp;, tensorflow::Var**, std::function&lt;tensorflow::Status (tensorflow::Var**)&gt;) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b50ac10)
    #6 0x1b512f1e in tensorflow::AssignVariableOp&lt;Eigen::ThreadPoolDevice, float&gt;::Compute(tensorflow::OpKernelContext*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1b512f1e)
    #7 0x1d1881c7 in tensorflow::ThreadPoolDevice::Compute(tensorflow::OpKernel*, tensorflow::OpKernelContext*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0x1d1881c7)
    #8 0xf96e0fe in tensorflow::KernelAndDevice::Run(std::vector&lt;tensorflow::Tensor, std::allocator&lt;tensorflow::Tensor&gt; &gt;*, std::vector&lt;tensorflow::Tensor, std::allocator&lt;tensorflow::Tensor&gt; &gt;*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf96e0fe)
    #9 0xf94f9c8 in TFE_Execute (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf94f9c8)
    #10 0xf94356d in TFE_Py_Execute(TFE_Context*, int, char const*, tensorflow::gtl::InlinedVector&lt;TFE_TensorHandle*, 4&gt;*, _object*, tensorflow::gtl::InlinedVector&lt;TFE_TensorHandle*, 2&gt;*, TF_Status*) (/build/cas/5d2/5d2be3b530580573ff7269adcab7cbac+0xf94356d)

PiperOrigin-RevId: 160160101

* Simplify strided_slice's shape handling

Now that TensorShape and PartialTensorShape share memory representations, there's no need for an abstract class that makes TensorShape and TensorShapeProto look the same.

RELNOTES: n/a
PiperOrigin-RevId: 160161618

* Added a tool to report the static information that can be extracted from a TF model.

PiperOrigin-RevId: 160162256

* Properly handle RefEnter, RefExit and RefNextIteration nodes.

PiperOrigin-RevId: 160162338

* Switch tfprof to use proto3

PiperOrigin-RevId: 160163483

* Fixes to cuda_config.h.

PiperOrigin-RevId: 160168545

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160171187

* Adds notes to prevent overfitting for Experiment continous_train_and_eval.

PiperOrigin-RevId: 160172692

* Go: Update generated wrapper functions for TensorFlow ops.

PiperOrigin-RevId: 160172985

* Merge changes from github.
END_PUBLIC

Note: this CL will break builds.  cl/159887762 to follow to fix all the breakages.

---
Commit 2336cdf7f authored by Maxwell Paul Brickner&lt;mbrickn@users.noreply.github.com&gt;
Committed by gunan&lt;gunan@google.com&gt;:
Updated link to use HTTPS (#10998)

Howdy!

I just updated a link to use https instead of http.

Thanks!
---
Commit ad0892df1 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] Fixes run_metadata_test for SYCL

 This test is designed to test CUDA specific behavior

---
Commit 6b37a0725 authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Update comments
---
Commit 1699d904a authored by John Lawson&lt;john@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] Fixes CUDA specific test run on SYCL (#56)

The testBadParentValuesOnGPU should only be run on CUDA devices, as the
test checks for particular CUDA behaviour. We don't actually provide a
SYCL kernel for GatherTree and so it's not a problem that the tests
don't target SYCL.
---
Commit 3c1946230 authored by myPrecious&lt;Moriadry@users.noreply.github.com&gt;
Committed by Shanqing Cai&lt;cais@google.com&gt;:
Java API to get the size of specified input list of operations. (#10865)

* Java API to get the size of specified input list of operations

* remove unnecessary explain to avoid bring a new term to users.

---
Commit e911c7480 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Luke Iwanski&lt;luke@codeplay.com&gt;:
[OpenCL] REGISTER -&gt; REGISTER6

---
Commit fbf6c4cec authored by superryanguo&lt;superryanguo@gmail.com&gt;
Committed by superryanguo&lt;superryanguo@gmail.com&gt;:
Simplify the Quickstart section with the weblink is better

---
Commit 72e2918cc authored by Taehoon Lee&lt;taehoonlee@snu.ac.kr&gt;
Committed by Taehoon Lee&lt;taehoonlee@snu.ac.kr&gt;:
Fix typos

---
Commit 90c4406b7 authored by Rishabh Patel&lt;patelrishabh@users.noreply.github.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Correct the learning rate as per the code snippet
---
Commit 03da61134 authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Update ir_array.cc
---
Commit 2df6cd3ac authored by Todd Wang&lt;toddwang@gmail.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Another try
---
Commit af0cbace1 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Transpose to go through Eigen (#10321)

---
Commit fc7361081 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Registers RGBToHSV and HSVToRGB (#91) (#10848)

* [OpenCL] Added RGBToHSV and HSVToRGB

* Aligning '\'
---
Commit 832894ef8 authored by Luke Iwanski&lt;luke@codeplay.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
[OpenCL] Registers AdjustContrastv2 (#10949)

* [OpenCL] Registers AdjustContrastv2 (#93)

* [OpenCL] Extended adjust_contrast_op_benchmark_test for OpenCL (#96)

* [OpenCL] Extended adjust_contrast_op_benchmark_test for OpenCL

* simplified to #ifndef

* Changed to &quot;#if GOOGLE_CUDA&quot;

* Update adjust_contrast_op_benchmark_test.cc

* Added comments

---
Commit cb4c2f8d1 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Make TransferBufferToInFeed not virual so it compiles.

---
Commit e89f04d80 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix calling Literal member functions.

---
Commit 15a8df724 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix mac build
clone from meheff's change:
[XLA] Change return type of DeviceAssignment::Deserialize to fix build
breakage on mac.
The mac build had the following error:

error: incomplete type 'xla::DeviceAssignment' used in type trait
expression

This was due to a static method returning a StatusOr&lt;DeviceAssignment&gt;
inside of the definition of DeviceAssignment.

---
Commit a54d43fa4 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Replace LiteralUtil to Literal in compiler/plugin/executor

---
Commit 88a6bb80c authored by Guenther Schmuelling&lt;guschmue@microsoft.com&gt;
Committed by Guenther Schmuelling&lt;guschmue@microsoft.com&gt;:
expand inline for debug builds to limit number of symbols

---
Commit 62fb49d31 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Fix visibility error for contrib/remote_fused_graph/pylib/BUILD.

---
Commit 4c75252f2 authored by Mark Neumann&lt;markn@allenai.org&gt;
Committed by Mark Neumann&lt;markn@allenai.org&gt;:
fix initial test values to avoid numerical instability

---
Commit b58d98353 authored by sj6077&lt;epik03sj@gmail.com&gt;
Committed by Benoit Steiner&lt;benoitsteiner@users.noreply.github.com&gt;:
Fixes of AutoParallel bug (#10368)

* Fix the bug that auto_parallel could replicate variable snapshot name

* Use NodeName in grappler:utils instead of substr, convert variables-&gt;variable_def of grappler item

* remove variable_def from grappler item, exclude snapshot nodes from dont_replicate_nodes in auto_parallel

---
Commit a286b7db8 authored by Yifei Feng&lt;yifeif@google.com&gt;
Committed by Yifei Feng&lt;yifeif@google.com&gt;:
Make debug_test slice integer.

---
Commit 97fcfdfa6 authored by Toby Boyd&lt;tobyboyd@google.com&gt;
Committed by GitHub&lt;noreply@github.com&gt;:
Fixed path to seq2seq.py and minor formatting
---
Commit 63c1befb8 authored by Anish Shah&lt;shah.anish07@gmail.com&gt;
Committed by Anish Shah&lt;shah.anish07@gmail.com&gt;:
Improve docs for tf.nn.depthwise_conv2d_native

---
Commit 8d42202b2 authored by Yong Tang&lt;yong.tang.github@outlook.com&gt;
Committed by Yong Tang&lt;yong.tang.github@outlook.com&gt;:
Fix mismatched delete in mkl_tfconv_op.cc

This fix fixes mismatched new[]-delete in mkl_tfconv_op.cc

(the file went through clang-format so there are some additional
changes)

Signed-off-by: Yong Tang &lt;yong.tang.github@outlook.com&gt;

---
Commit 26301bd55 authored by Danny Goodman&lt;goodman.danny@gmail.com&gt;
Committed by Danny Goodman&lt;goodman.danny@gmail.com&gt;:
fix error format

---
Commit b3f33ad46 authored by Yao Zhang&lt;yaozhang@google.com&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Make changes to prepare for the fused option of batch norm to be set to None (None means using fused batch norm if possible).

PiperOrigin-RevId: 159649743

---
Commit a4a469832 authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
[XLA] Add tests for select ops and while loops that produce tuples that contain predicates.

PiperOrigin-RevId: 159645900

---
Commit 980d3f2be authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Use C API to implement Operation.name property

This name property is used in many existing tests including those that
already run with C API enabled (math_ops_test, framework_ops_test,
session_test, session_partial_run_test, math_ops_test_gpu, etc).

PiperOrigin-RevId: 159645767

---
Commit 26239c706 authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
Previously we didn't have an implementation of BatchNormInference and BatchNormTraining, which gives a linker error if anyone ever tries to call that. A dummy implementation is friendlier than a linker error.

PiperOrigin-RevId: 159645612

---
Commit f671c5caa authored by A. Unique TensorFlower&lt;gardener@tensorflow.org&gt;
Committed by TensorFlower Gardener&lt;gardener@tensorflow.org&gt;:
BEGIN_PUBLIC
Automated g4 rollback of changelist 159570549

PiperOrigin-RevId: 160182040

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160183349

* Merge changes from github followup.

PiperOrigin-RevId: 160183498

* Automated g4 rollback of changelist 160183498

PiperOrigin-RevId: 160189134

* Automated g4 rollback of changelist 160182040

PiperOrigin-RevId: 160190881

* [XLA] Disallow fuse X into Y if there are paths from X to Y which don't fuse

Just because X can fuse into all of its consumers does not mean that those
consumers can fuse into anything. Depending on the structure of the graph, this
can either result in no performance win at all or, in the case of recurrent
networks, a big performance deficit.

PiperOrigin-RevId: 160194058

* First draft of Tensors segment of the programmer's guide.

PiperOrigin-RevId: 160196550

* First draft of variables unit of programmer's guide.

PiperOrigin-RevId: 160196566

* Make xla::Literal moveable.

PiperOrigin-RevId: 160197273

* Automated g4 rollback of changelist 159897279

PiperOrigin-RevId: 160198598

* Updates text_classification example.

PiperOrigin-RevId: 160200457

* Fix backward compatibility test broken by rollback.

PiperOrigin-RevId: 160222187

* Support advisor in all places (Command line, APIs)
Add expensive operation checker

PiperOrigin-RevId: 160222348

* [XLA] Simplify the fusion heuristic

We had two different aspects of the fusion heuristic:
- Don't fuse a producer into a consumer if there exists a path from the
  producer to the consumer which cannot be fused.
- Don't fuse a producer into a consumer if any consumer of the producer cannot
  fuse.

These can be combined into one, simpler, heuristic.

PiperOrigin-RevId: 160222771

* Automated g4 rollback of changelist 160196566

PiperOrigin-RevId: 160222930

* Automated g4 rollback of changelist 160196550

PiperOrigin-RevId: 160222942

* Lets the HParam parser also accept True and False as inputs, since that's how python prints booleans.

PiperOrigin-RevId: 160234658

* Automated g4 rollback of changelist 155070869

PiperOrigin-RevId: 160249526

* [TF:XLA] Inline the sigmoid operation instead of mapping it elementwise.

PiperOrigin-RevId: 160274436

* Make sure all convolution tests are testing non-trivial cases, i.e. where not all inputs are 0, leading to an all-0 output, which masks most possible bugs.
We do not check-fail on 0-sized dimensions as tests for these special cases
exist.

PiperOrigin-RevId: 160274593

* Explicitly use &quot;dns&quot; URI scheme when using DNS names or literal IP
addresses with gRPC.  This avoids problems in environments in which the
default URI scheme is something other than &quot;dns&quot;.

PiperOrigin-RevId: 160276862

* Add RWSE (root weighted squared error) to the WALS estimator.

PiperOrigin-RevId: 160276937

* Don't include node_def.proto.h in node_def_util.h

The goal is to make kernels mostly independent of proto headers, which will let us lock down our .so imports.

RELNOTES: n/a
PiperOrigin-RevId: 160278032

* [XLA] Add tuple support to Literal::CreateFromShape.

PiperOrigin-RevId: 160278561

* Updates some more examples in examples/learn.

PiperOrigin-RevId: 160278757

* Automated g4 rollback of changelist 160278032

PiperOrigin-RevId: 160280961

* Fixed the bug that Estimator does not make deepcopy of params in constructor

PiperOrigin-RevId: 160281247

* Clean out the config and params in TPUEstimator.

PiperOrigin-RevId: 160281507

* [XLA] Remove the &quot;hlo dumper&quot; parameter of xla::Compiler and its piping.

This dumper is no longer necessary since the restructuring of HLO dumping and
the addition of MaybeDumpHloModule which heeds to the right flags. The
remaining bits didn't have additional functionality, but constituted a lot of
boilerplate that has to be propagated throughout the backends.

PiperOrigin-RevId: 160281798

* [TF:XLA] Refactor the sigmoid op as a rescaled tanh.

PiperOrigin-RevId: 160282472

* Fix uninitialized values in TensorForest code.

PiperOrigin-RevId: 160284420

* [TF:XLA] Update Tensorflow LLVM release to upstream r306370.

Fix broken XLA build.

PiperOrigin-RevId: 160284588

* tfdbg example: fix --tensor_size issue in debug_fibonacci

PiperOrigin-RevId: 160290541

* [SE] ThenConvolveWithAlgorithm vlogs algorithm configs.

PiperOrigin-RevId: 160292762

* Fix documentation of Estimator class (invalid quotes).

PiperOrigin-RevId: 160292803

* Shrink the test size to avoid OOM error on old GPUs.

PiperOrigin-RevId: 160292834

* [TF:XLA] Reject operators with resource outputs on CPU and GPU devices.

We were checking for resource inputs but not resource outputs, which led to accidental fusion of some TensorArray ops on CPU and GPU.

PiperOrigin-RevId: 160294302

* Add a functionality of remote fused graph transformation to fuse graphs by op type

PiperOrigin-RevId: 160300039

* Cudnn compatible LSTMCell and LSTMBlockCell

PiperOrigin-RevId: 160300668

* [XLA] Remove &quot;operand&quot; argument from HandleReducePrecision.

PiperOrigin-RevId: 160301461

* Added more reduce window tests.

PiperOrigin-RevId: 160301509

* Updates more text classification examples in examples/learn.

PiperOrigin-RevId: 160305131

* Use C API to implement Operation._output_types

This change first converts the _output_types member to a property and
then implements it using C API if it is enabled.

PiperOrigin-RevId: 160306227

* Add more tests for BatchNormTraining.
RELNOTES: n/a

PiperOrigin-RevId: 160307959

* Update path to print_selective_registration_header.py in comment

PiperOrigin-RevId: 160308173

* Migrate TensorForest v4 python to contrib.

PiperOrigin-RevId: 160308805

* Automated g4 rollback of changelist 159454657

PiperOrigin-RevId: 160314706

* TESTFIX:  distributions:trig_test wasn't passing in ASAN mode.

PiperOrigin-RevId: 160315597

* tfdbg doc: fixes and improvements

PiperOrigin-RevId: 160318411

* Add a time estimation to HloCostAnalysis and represent properties as a map so that adding more properties will be easier, e.g. in a sub-class.

PiperOrigin-RevId: 160318494

* tfdbg: revert dns:/// prefix in gRPC mode

PiperOrigin-RevId: 160319348

* Moves TensorCApi from c_api.cc to c_api_internal.h, where it can be used
by other code that require access to the underlying TensorBuffers.

PiperOrigin-RevId: 160323362

* Readd the new tensors and variables documents, with tests passing.

PiperOrigin-RevId: 160324191

* Make ResourceHandle not be a proto

I'm trying to make core/kernels independent of protos.  Currently the dtype ResourceHandle is itself a proto.  After this CL, ResourceHandle is a normal C++ type which gets converted to/from ResourceHandleProto at (de)serialization time.

RELNOTES: n/a
PiperOrigin-RevId: 160329002

* Minor cleanup: remove unused dependencies and inclusions

PiperOrigin-RevId: 160334030

* Add name_scopes to mnist_deep.py for a cleaner graph layout.

PiperOrigin-RevId: 160338775

* Add note about `tf.test.mock` to docs for `tf.test`

PiperOrigin-RevId: 160338811

* Internal change.

PiperOrigin-RevId: 160339087

* Fix bugs in ScatterNd and add ScatterNdNonAliasingAdd.

tf.scatter_nd_non_aliasing_add acts similarly to tf.scatter_nd_add but
works on non-ref objects (i.e., Tensors -- not Variables).  This means
it has a gradient with respect to the primary input as well as the
updates.  It does its best to avoid making extra copies of the input.

PiperOrigin-RevId: 160339328

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160340888

* Add checkpoint conversion for models that use the attention mechanism implemented in tensorflow/contrib/legacy_seq2seq/python/ops/seq2seq.py.

PiperOrigin-RevId: 160340994

* Go: Update generated wrapper functions for TensorFlow ops.

PiperOrigin-RevId: 160341769

* Merge changes from github.

PiperOrigin-RevId: 160344052

* Update ops-related pbtxt files.

PiperOrigin-RevId: 160346151

* Load py_test in tensorflow/contrib/boosted_trees/BUILD to fix pip test
visibility failures.

* Disable boosted_trees tests on mac while they are being debugged.">)</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>13</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="ebrevdo" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=ebrevdo"><img alt="@ebrevdo" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1794715?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tensorflower-gardener" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=tensorflower-gardener"><img alt="@tensorflower-gardener" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/17151892?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="taehoonlee" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=taehoonlee"><img alt="@taehoonlee" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/4445535?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="jhseu" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=jhseu"><img alt="@jhseu" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/170179?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="yifeif" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=yifeif"><img alt="@yifeif" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1192265?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="xiejw" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=xiejw"><img alt="@xiejw" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/1184671?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="martinwicke" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=martinwicke"><img alt="@martinwicke" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/577277?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="m-colombo" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=m-colombo"><img alt="@m-colombo" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/8291084?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="protoget" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=protoget"><img alt="@protoget" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/5117188?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="fchollet" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=fchollet"><img alt="@fchollet" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/710255?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="drpngx" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=drpngx"><img alt="@drpngx" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/20959853?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="caisq" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=caisq"><img alt="@caisq" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/16824702?v=4&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="kosklain" href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py?author=kosklain"><img alt="@kosklain" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1104579?v=4&amp;s=40" width="20" /> </a>


    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@ebrevdo" height="24" src="https://avatars3.githubusercontent.com/u/1794715?v=4&amp;s=48" width="24" />
            <a href="/ebrevdo">ebrevdo</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@tensorflower-gardener" height="24" src="https://avatars0.githubusercontent.com/u/17151892?v=4&amp;s=48" width="24" />
            <a href="/tensorflower-gardener">tensorflower-gardener</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@taehoonlee" height="24" src="https://avatars0.githubusercontent.com/u/4445535?v=4&amp;s=48" width="24" />
            <a href="/taehoonlee">taehoonlee</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@jhseu" height="24" src="https://avatars0.githubusercontent.com/u/170179?v=4&amp;s=48" width="24" />
            <a href="/jhseu">jhseu</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@yifeif" height="24" src="https://avatars3.githubusercontent.com/u/1192265?v=4&amp;s=48" width="24" />
            <a href="/yifeif">yifeif</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@xiejw" height="24" src="https://avatars1.githubusercontent.com/u/1184671?v=4&amp;s=48" width="24" />
            <a href="/xiejw">xiejw</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@martinwicke" height="24" src="https://avatars0.githubusercontent.com/u/577277?v=4&amp;s=48" width="24" />
            <a href="/martinwicke">martinwicke</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@m-colombo" height="24" src="https://avatars1.githubusercontent.com/u/8291084?v=4&amp;s=48" width="24" />
            <a href="/m-colombo">m-colombo</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@protoget" height="24" src="https://avatars3.githubusercontent.com/u/5117188?v=4&amp;s=48" width="24" />
            <a href="/protoget">protoget</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@fchollet" height="24" src="https://avatars3.githubusercontent.com/u/710255?v=4&amp;s=48" width="24" />
            <a href="/fchollet">fchollet</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@drpngx" height="24" src="https://avatars2.githubusercontent.com/u/20959853?v=4&amp;s=48" width="24" />
            <a href="/drpngx">drpngx</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@caisq" height="24" src="https://avatars1.githubusercontent.com/u/16824702?v=4&amp;s=48" width="24" />
            <a href="/caisq">caisq</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@kosklain" height="24" src="https://avatars3.githubusercontent.com/u/1104579?v=4&amp;s=48" width="24" />
            <a href="/kosklain">kosklain</a>
          </li>
      </ul>
    </div>
  </div>

  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/tensorflow/tensorflow/raw/r1.3/tensorflow/python/ops/rnn_cell_impl.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/tensorflow/tensorflow/blame/r1.3/tensorflow/python/ops/rnn_cell_impl.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/tensorflow/tensorflow/commits/r1.3/tensorflow/python/ops/rnn_cell_impl.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      1055 lines (881 sloc)
      <span class="file-info-divider"></span>
    39.8 KB
  </div>
</div>

    

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Copyright 2015 The TensorFlow Authors. All Rights Reserved.</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> you may not use this file except in compliance with the License.</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> You may obtain a copy of the License at</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>     http://www.apache.org/licenses/LICENSE-2.0</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Unless required by applicable law or agreed to in writing, software</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> See the License for the specific language governing permissions and</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> limitations under the License.</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> ==============================================================================</span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Module implementing RNN Cells.</span></td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-s">This module provides a number of basic commonly used RNN cells, such as LSTM</span></td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-s">(Long Short Term Memory) or GRU (Gated Recurrent Unit), and a number of</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-s">operators that allow adding dropouts, projections, or embeddings for inputs.</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Constructing multi-layer cells is supported by the class `MultiRNNCell`, or by</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-s">calling the `rnn` ops several times.</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> absolute_import</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> division</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> <span class="pl-c1">__future__</span> <span class="pl-k">import</span> print_function</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> collections</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> hashlib</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> numbers</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.framework <span class="pl-k">import</span> constant_op</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.framework <span class="pl-k">import</span> dtypes</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.framework <span class="pl-k">import</span> ops</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.framework <span class="pl-k">import</span> tensor_shape</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.framework <span class="pl-k">import</span> tensor_util</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.layers <span class="pl-k">import</span> base <span class="pl-k">as</span> base_layer</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> array_ops</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> clip_ops</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> init_ops</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> math_ops</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> nn_ops</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> partitioned_variables</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> random_ops</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> variable_scope <span class="pl-k">as</span> vs</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.ops <span class="pl-k">import</span> variables <span class="pl-k">as</span> tf_variables</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.platform <span class="pl-k">import</span> tf_logging <span class="pl-k">as</span> logging</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> tensorflow.python.util <span class="pl-k">import</span> nest</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_BIAS_VARIABLE_NAME</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>bias<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_WEIGHTS_VARIABLE_NAME</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>kernel<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_like_rnncell</span>(<span class="pl-smi">cell</span>):</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Checks that a given object is an RNNCell by using duck typing.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">  conditions <span class="pl-k">=</span> [<span class="pl-c1">hasattr</span>(cell, <span class="pl-s"><span class="pl-pds">&quot;</span>output_size<span class="pl-pds">&quot;</span></span>), <span class="pl-c1">hasattr</span>(cell, <span class="pl-s"><span class="pl-pds">&quot;</span>state_size<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">hasattr</span>(cell, <span class="pl-s"><span class="pl-pds">&quot;</span>zero_state<span class="pl-pds">&quot;</span></span>), <span class="pl-c1">callable</span>(cell)]</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> <span class="pl-c1">all</span>(conditions)</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_concat</span>(<span class="pl-smi">prefix</span>, <span class="pl-smi">suffix</span>, <span class="pl-smi">static</span><span class="pl-k">=</span><span class="pl-c1">False</span>):</td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Concat that enables int, Tensor, or TensorShape values.</span></td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  This function takes a size specification, which can be an integer, a</span></td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  TensorShape, or a Tensor, and converts it into a concatenated Tensor</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  (if static = False) or a list of integers (if static = True).</span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Args:</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    prefix: The prefix; usually the batch size (and/or time step size).</span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      (TensorShape, int, or Tensor.)</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    suffix: TensorShape, int, or Tensor.</span></td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    static: If `True`, return a python list with possibly unknown dimensions.</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      Otherwise return a `Tensor`.</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Returns:</span></td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    shape: the concatenation of prefix and suffix.</span></td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Raises:</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    ValueError: if `suffix` is not a scalar or vector (or TensorShape).</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    ValueError: if prefix or suffix was `None` and asked for dynamic</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      Tensors out.</span></td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(prefix, ops.Tensor):</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    p <span class="pl-k">=</span> prefix</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    p_static <span class="pl-k">=</span> tensor_util.constant_value(prefix)</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> p.shape.ndims <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">      p <span class="pl-k">=</span> array_ops.expand_dims(p, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> p.shape.ndims <span class="pl-k">!=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>prefix tensor must be either a scalar or vector, <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&quot;</span>but saw tensor: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> p)</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    p <span class="pl-k">=</span> tensor_shape.as_shape(prefix)</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    p_static <span class="pl-k">=</span> p.as_list() <span class="pl-k">if</span> p.ndims <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    p <span class="pl-k">=</span> (constant_op.constant(p.as_list(), <span class="pl-v">dtype</span><span class="pl-k">=</span>dtypes.int32)</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">         <span class="pl-k">if</span> p.is_fully_defined() <span class="pl-k">else</span> <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(suffix, ops.Tensor):</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    s <span class="pl-k">=</span> suffix</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    s_static <span class="pl-k">=</span> tensor_util.constant_value(suffix)</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> s.shape.ndims <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">      s <span class="pl-k">=</span> array_ops.expand_dims(s, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> s.shape.ndims <span class="pl-k">!=</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>suffix tensor must be either a scalar or vector, <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&quot;</span>but saw tensor: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> s)</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">    s <span class="pl-k">=</span> tensor_shape.as_shape(suffix)</td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">    s_static <span class="pl-k">=</span> s.as_list() <span class="pl-k">if</span> s.ndims <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">    s <span class="pl-k">=</span> (constant_op.constant(s.as_list(), <span class="pl-v">dtype</span><span class="pl-k">=</span>dtypes.int32)</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">         <span class="pl-k">if</span> s.is_fully_defined() <span class="pl-k">else</span> <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> static:</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">    shape <span class="pl-k">=</span> tensor_shape.as_shape(p_static).concatenate(s_static)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">    shape <span class="pl-k">=</span> shape.as_list() <span class="pl-k">if</span> shape.ndims <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> p <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">or</span> s <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Provided a prefix or suffix of None: <span class="pl-c1">%s</span> and <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">                       <span class="pl-k">%</span> (prefix, suffix))</td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">    shape <span class="pl-k">=</span> array_ops.concat((p, s), <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> shape</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_zero_state_tensors</span>(<span class="pl-smi">state_size</span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create tensors of zeros based on state_size, batch_size, and dtype.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">get_state_shape</span>(<span class="pl-smi">s</span>):</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Combine s with batch_size to get a proper tensor shape.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">    c <span class="pl-k">=</span> _concat(batch_size, s)</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">    c_static <span class="pl-k">=</span> _concat(batch_size, s, <span class="pl-v">static</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">    size <span class="pl-k">=</span> array_ops.zeros(c, <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">    size.set_shape(c_static)</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> size</td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> nest.map_structure(get_state_shape, state_size)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">RNNCell</span>(<span class="pl-e">base_layer</span>.<span class="pl-e">Layer</span>):</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Abstract object representing an RNN cell.</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Every `RNNCell` must have the properties below and implement `call` with</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  the signature `(output, next_state) = call(input, state)`.  The optional</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  third input argument, `scope`, is allowed for backwards compatibility</span></td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  purposes; but should be left off for new subclasses.</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  This definition of cell differs from the definition used in the literature.</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  In the literature, &#39;cell&#39; refers to an object with a single scalar output.</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  This definition refers to a horizontal array of such units.</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  An RNN cell, in the most abstract setting, is anything that has</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  a state and performs some operation that takes a matrix of inputs.</span></td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  This operation results in an output matrix with `self.output_size` columns.</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  If `self.state_size` is an integer, this operation also results in a new</span></td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  state matrix with `self.state_size` columns.  If `self.state_size` is a</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  (possibly nested tuple of) TensorShape object(s), then it should return a</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  matching structure of Tensors having shape `[batch_size].concatenate(s)`</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  for each `s` in `self.batch_size`.</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__call__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>, <span class="pl-smi">scope</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run this RNN cell on inputs, starting from the given state.</span></td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      inputs: `2-D` tensor with shape `[batch_size x input_size]`.</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state: if `self.state_size` is an integer, this should be a `2-D Tensor`</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        with shape `[batch_size x self.state_size]`.  Otherwise, if</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `self.state_size` is a tuple of integers, this should be a tuple</span></td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        with shapes `[batch_size x s] for s in self.state_size`.</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      scope: VariableScope for the created subgraph; defaults to class name.</span></td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Returns:</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      A pair containing:</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - Output: A `2-D` tensor with shape `[batch_size x self.output_size]`.</span></td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - New state: Either a single `2-D` tensor, or a tuple of tensors matching</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the arity and shapes of `state`.</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> scope <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">with</span> vs.variable_scope(scope,</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">                             <span class="pl-v">custom_getter</span><span class="pl-k">=</span><span class="pl-c1">self</span>._rnn_get_variable) <span class="pl-k">as</span> scope:</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">super</span>(RNNCell, <span class="pl-c1">self</span>).<span class="pl-c1">__call__</span>(inputs, state, <span class="pl-v">scope</span><span class="pl-k">=</span>scope)</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">with</span> vs.variable_scope(vs.get_variable_scope(),</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">                             <span class="pl-v">custom_getter</span><span class="pl-k">=</span><span class="pl-c1">self</span>._rnn_get_variable):</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">super</span>(RNNCell, <span class="pl-c1">self</span>).<span class="pl-c1">__call__</span>(inputs, state)</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">_rnn_get_variable</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">getter</span>, <span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">    variable <span class="pl-k">=</span> getter(<span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line">    trainable <span class="pl-k">=</span> (variable <span class="pl-k">in</span> tf_variables.trainable_variables() <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">                 (<span class="pl-c1">isinstance</span>(variable, tf_variables.PartitionedVariable) <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">                  <span class="pl-c1">list</span>(variable)[<span class="pl-c1">0</span>] <span class="pl-k">in</span> tf_variables.trainable_variables()))</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> trainable <span class="pl-k">and</span> variable <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>._trainable_weights:</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._trainable_weights.append(variable)</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">elif</span> <span class="pl-k">not</span> trainable <span class="pl-k">and</span> variable <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>._non_trainable_weights:</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._non_trainable_weights.append(variable)</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> variable</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>size(s) of state(s) used by this cell.</span></td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    It can be represented by an Integer, a TensorShape or a tuple of Integers</span></td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    or TensorShapes.</span></td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> <span class="pl-c1">NotImplementedError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Abstract method<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Integer or TensorShape: size of outputs produced by this cell.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> <span class="pl-c1">NotImplementedError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Abstract method<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">build</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">_</span>):</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> This tells the parent Layer object that it&#39;s OK to call</span></td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> self.add_variable() inside the call() method.</span></td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">zero_state</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Return zero-filled state tensor(s).</span></td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      batch_size: int, float, or unit Tensor representing the batch size.</span></td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      dtype: the data type to use for the state.</span></td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Returns:</span></td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      If `state_size` is an int or TensorShape, then the return value is a</span></td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      `N-D` tensor of shape `[batch_size x state_size]` filled with zeros.</span></td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      If `state_size` is a nested list or tuple, then the return value is</span></td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      a nested list or tuple (of the same structure) of `2-D` tensors with</span></td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      the shapes `[batch_size x s]` for each s in `state_size`.</span></td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-c1">type</span>(<span class="pl-c1">self</span>).<span class="pl-c1">__name__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZeroState<span class="pl-pds">&quot;</span></span>, <span class="pl-v">values</span><span class="pl-k">=</span>[batch_size]):</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">      state_size <span class="pl-k">=</span> <span class="pl-c1">self</span>.state_size</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> _zero_state_tensors(state_size, batch_size, dtype)</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">BasicRNNCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>The most basic RNN cell.</span></td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Args:</span></td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    num_units: int, The number of units in the RNN cell.</span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    activation: Nonlinearity to use.  Default: `tanh`.</span></td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    reuse: (optional) Python boolean describing whether to reuse variables</span></td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line"><span class="pl-s">     in an existing scope.  If not `True`, and the existing scope already has</span></td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line"><span class="pl-s">     the given variables, an error is raised.</span></td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">num_units</span>, <span class="pl-smi">activation</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">reuse</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">super</span>(BasicRNNCell, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(<span class="pl-v">_reuse</span><span class="pl-k">=</span>reuse)</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_units <span class="pl-k">=</span> num_units</td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._activation <span class="pl-k">=</span> activation <span class="pl-k">or</span> math_ops.tanh</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._num_units</td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._num_units</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>):</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Most basic RNN: output = new_state = act(W * input + U * state + B).<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">    output <span class="pl-k">=</span> <span class="pl-c1">self</span>._activation(_linear([inputs, state], <span class="pl-c1">self</span>._num_units, <span class="pl-c1">True</span>))</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> output, output</td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">GRUCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Gated Recurrent Unit cell (cf. http://arxiv.org/abs/1406.1078).<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>,</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">num_units</span>,</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">activation</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">reuse</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">kernel_initializer</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">bias_initializer</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">super</span>(GRUCell, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(<span class="pl-v">_reuse</span><span class="pl-k">=</span>reuse)</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_units <span class="pl-k">=</span> num_units</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._activation <span class="pl-k">=</span> activation <span class="pl-k">or</span> math_ops.tanh</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._kernel_initializer <span class="pl-k">=</span> kernel_initializer</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._bias_initializer <span class="pl-k">=</span> bias_initializer</td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._num_units</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._num_units</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>):</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Gated recurrent unit (GRU) with nunits cells.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> vs.variable_scope(<span class="pl-s"><span class="pl-pds">&quot;</span>gates<span class="pl-pds">&quot;</span></span>):  <span class="pl-c"><span class="pl-c">#</span> Reset gate and update gate.</span></td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">      <span class="pl-c"><span class="pl-c">#</span> We start with bias of 1.0 to not reset and not update.</span></td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">      bias_ones <span class="pl-k">=</span> <span class="pl-c1">self</span>._bias_initializer</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._bias_initializer <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">        dtype <span class="pl-k">=</span> [a.dtype <span class="pl-k">for</span> a <span class="pl-k">in</span> [inputs, state]][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">        bias_ones <span class="pl-k">=</span> init_ops.constant_initializer(<span class="pl-c1">1.0</span>, <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">      value <span class="pl-k">=</span> math_ops.sigmoid(</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">          _linear([inputs, state], <span class="pl-c1">2</span> <span class="pl-k">*</span> <span class="pl-c1">self</span>._num_units, <span class="pl-c1">True</span>, bias_ones,</td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">                  <span class="pl-c1">self</span>._kernel_initializer))</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">      r, u <span class="pl-k">=</span> array_ops.split(<span class="pl-v">value</span><span class="pl-k">=</span>value, <span class="pl-v">num_or_size_splits</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> vs.variable_scope(<span class="pl-s"><span class="pl-pds">&quot;</span>candidate<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">      c <span class="pl-k">=</span> <span class="pl-c1">self</span>._activation(</td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">          _linear([inputs, r <span class="pl-k">*</span> state], <span class="pl-c1">self</span>._num_units, <span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">                  <span class="pl-c1">self</span>._bias_initializer, <span class="pl-c1">self</span>._kernel_initializer))</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">    new_h <span class="pl-k">=</span> u <span class="pl-k">*</span> state <span class="pl-k">+</span> (<span class="pl-c1">1</span> <span class="pl-k">-</span> u) <span class="pl-k">*</span> c</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> new_h, new_h</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">_LSTMStateTuple <span class="pl-k">=</span> collections.namedtuple(<span class="pl-s"><span class="pl-pds">&quot;</span>LSTMStateTuple<span class="pl-pds">&quot;</span></span>, (<span class="pl-s"><span class="pl-pds">&quot;</span>c<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>h<span class="pl-pds">&quot;</span></span>))</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">LSTMStateTuple</span>(<span class="pl-e">_LSTMStateTuple</span>):</td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Tuple used by LSTM Cells for `state_size`, `zero_state`, and output state.</span></td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Stores two elements: `(c, h)`, in that order.</span></td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Only used when `state_is_tuple=True`.</span></td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">  <span class="pl-c1">__slots__</span> <span class="pl-k">=</span> ()</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">dtype</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">    (c, h) <span class="pl-k">=</span> <span class="pl-c1">self</span></td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> c.dtype <span class="pl-k">!=</span> h.dtype:</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Inconsistent internal state: <span class="pl-c1">%s</span> vs <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">                      (<span class="pl-c1">str</span>(c.dtype), <span class="pl-c1">str</span>(h.dtype)))</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> c.dtype</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">BasicLSTMCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Basic LSTM recurrent network cell.</span></td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  The implementation is based on: http://arxiv.org/abs/1409.2329.</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  We add forget_bias (default: 1) to the biases of the forget gate in order to</span></td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  reduce the scale of forgetting in the beginning of the training.</span></td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  It does not allow cell clipping, a projection layer, and does not</span></td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  use peep-hole connections: it is the basic baseline.</span></td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  For advanced models, please use the full @{tf.nn.rnn_cell.LSTMCell}</span></td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  that follows.</span></td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">num_units</span>, <span class="pl-smi">forget_bias</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>,</td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">state_is_tuple</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">activation</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">reuse</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Initialize the basic LSTM cell.</span></td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      num_units: int, The number of units in the LSTM cell.</span></td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      forget_bias: float, The bias added to forget gates (see above).</span></td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Must set to `0.0` manually when restoring from CudnnLSTM-trained</span></td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        checkpoints.</span></td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state_is_tuple: If True, accepted and returned states are 2-tuples of</span></td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the `c_state` and `m_state`.  If False, they are concatenated</span></td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        along the column axis.  The latter behavior will soon be deprecated.</span></td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      activation: Activation function of the inner states.  Default: `tanh`.</span></td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      reuse: (optional) Python boolean describing whether to reuse variables</span></td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        in an existing scope.  If not `True`, and the existing scope already has</span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the given variables, an error is raised.</span></td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      When restoring from CudnnLSTM-trained checkpoints, must use</span></td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      CudnnCompatibleLSTMCell instead.</span></td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">super</span>(BasicLSTMCell, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(<span class="pl-v">_reuse</span><span class="pl-k">=</span>reuse)</td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">      logging.warn(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>: Using a concatenated state is slower and will soon be <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span>deprecated.  Use state_is_tuple=True.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_units <span class="pl-k">=</span> num_units</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._forget_bias <span class="pl-k">=</span> forget_bias</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">=</span> state_is_tuple</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._activation <span class="pl-k">=</span> activation <span class="pl-k">or</span> math_ops.tanh</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> (LSTMStateTuple(<span class="pl-c1">self</span>._num_units, <span class="pl-c1">self</span>._num_units)</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">else</span> <span class="pl-c1">2</span> <span class="pl-k">*</span> <span class="pl-c1">self</span>._num_units)</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._num_units</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>):</td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Long short-term memory cell (LSTM).</span></td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      inputs: `2-D` tensor with shape `[batch_size x input_size]`.</span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state: An `LSTMStateTuple` of state tensors, each shaped</span></td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `[batch_size x self.state_size]`, if `state_is_tuple` has been set to</span></td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `True`.  Otherwise, a `Tensor` shaped</span></td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `[batch_size x 2 * self.state_size]`.</span></td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Returns:</span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      A pair containing the new hidden state, and the new state (either a</span></td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `LSTMStateTuple` or a concatenated state, depending on</span></td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `state_is_tuple`).</span></td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">    sigmoid <span class="pl-k">=</span> math_ops.sigmoid</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Parameters of gates are concatenated into one multiply for efficiency.</span></td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">      c, h <span class="pl-k">=</span> state</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">      c, h <span class="pl-k">=</span> array_ops.split(<span class="pl-v">value</span><span class="pl-k">=</span>state, <span class="pl-v">num_or_size_splits</span><span class="pl-k">=</span><span class="pl-c1">2</span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">    concat <span class="pl-k">=</span> _linear([inputs, h], <span class="pl-c1">4</span> <span class="pl-k">*</span> <span class="pl-c1">self</span>._num_units, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> i = input_gate, j = new_input, f = forget_gate, o = output_gate</span></td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    i, j, f, o <span class="pl-k">=</span> array_ops.split(<span class="pl-v">value</span><span class="pl-k">=</span>concat, <span class="pl-v">num_or_size_splits</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">    new_c <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line">        c <span class="pl-k">*</span> sigmoid(f <span class="pl-k">+</span> <span class="pl-c1">self</span>._forget_bias) <span class="pl-k">+</span> sigmoid(i) <span class="pl-k">*</span> <span class="pl-c1">self</span>._activation(j))</td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">    new_h <span class="pl-k">=</span> <span class="pl-c1">self</span>._activation(new_c) <span class="pl-k">*</span> sigmoid(o)</td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">      new_state <span class="pl-k">=</span> LSTMStateTuple(new_c, new_h)</td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">      new_state <span class="pl-k">=</span> array_ops.concat([new_c, new_h], <span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> new_h, new_state</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">LSTMCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Long short-term memory unit (LSTM) recurrent network cell.</span></td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  The default non-peephole implementation is based on:</span></td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    http://www.bioinf.jku.at/publications/older/2604.pdf</span></td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  S. Hochreiter and J. Schmidhuber.</span></td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  &quot;Long Short-Term Memory&quot;. Neural Computation, 9(8):1735-1780, 1997.</span></td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  The peephole implementation is based on:</span></td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    https://research.google.com/pubs/archive/43905.pdf</span></td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Hasim Sak, Andrew Senior, and Francoise Beaufays.</span></td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  &quot;Long short-term memory recurrent neural network architectures for</span></td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line"><span class="pl-s">   large scale acoustic modeling.&quot; INTERSPEECH, 2014.</span></td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  The class uses optional peep-hole connections, optional cell clipping, and</span></td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  an optional projection layer.</span></td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">num_units</span>,</td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">use_peepholes</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-smi">cell_clip</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">initializer</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">num_proj</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">proj_clip</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">num_unit_shards</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">num_proj_shards</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">forget_bias</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>, <span class="pl-smi">state_is_tuple</span><span class="pl-k">=</span><span class="pl-c1">True</span>,</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">activation</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">reuse</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Initialize the parameters for an LSTM cell.</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      num_units: int, The number of units in the LSTM cell</span></td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      use_peepholes: bool, set True to enable diagonal/peephole connections.</span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cell_clip: (optional) A float value, if provided the cell state is clipped</span></td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        by this value prior to the cell output activation.</span></td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      initializer: (optional) The initializer to use for the weight and</span></td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        projection matrices.</span></td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      num_proj: (optional) int, The output dimensionality for the projection</span></td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        matrices.  If None, no projection is performed.</span></td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      proj_clip: (optional) A float value.  If `num_proj &gt; 0` and `proj_clip` is</span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        provided, then the projected values are clipped elementwise to within</span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `[-proj_clip, proj_clip]`.</span></td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      num_unit_shards: Deprecated, will be removed by Jan. 2017.</span></td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Use a variable_scope partitioner instead.</span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      num_proj_shards: Deprecated, will be removed by Jan. 2017.</span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Use a variable_scope partitioner instead.</span></td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      forget_bias: Biases of the forget gate are initialized by default to 1</span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        in order to reduce the scale of forgetting at the beginning of</span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the training. Must set it manually to `0.0` when restoring from</span></td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        CudnnLSTM trained checkpoints.</span></td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state_is_tuple: If True, accepted and returned states are 2-tuples of</span></td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the `c_state` and `m_state`.  If False, they are concatenated</span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        along the column axis.  This latter behavior will soon be deprecated.</span></td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      activation: Activation function of the inner states.  Default: `tanh`.</span></td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      reuse: (optional) Python boolean describing whether to reuse variables</span></td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        in an existing scope.  If not `True`, and the existing scope already has</span></td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the given variables, an error is raised.</span></td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      When restoring from CudnnLSTM-trained checkpoints, must use</span></td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      CudnnCompatibleLSTMCell instead.</span></td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">super</span>(LSTMCell, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(<span class="pl-v">_reuse</span><span class="pl-k">=</span>reuse)</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">      logging.warn(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>: Using a concatenated state is slower and will soon be <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span>deprecated.  Use state_is_tuple=True.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> num_unit_shards <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">or</span> num_proj_shards <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">      logging.warn(</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">          <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>: The num_unit_shards and proj_unit_shards parameters are <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">          <span class="pl-s"><span class="pl-pds">&quot;</span>deprecated and will be removed in Jan 2017.  <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">          <span class="pl-s"><span class="pl-pds">&quot;</span>Use a variable scope with a partitioner instead.<span class="pl-pds">&quot;</span></span>, <span class="pl-c1">self</span>)</td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_units <span class="pl-k">=</span> num_units</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._use_peepholes <span class="pl-k">=</span> use_peepholes</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell_clip <span class="pl-k">=</span> cell_clip</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._initializer <span class="pl-k">=</span> initializer</td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_proj <span class="pl-k">=</span> num_proj</td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._proj_clip <span class="pl-k">=</span> proj_clip</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_unit_shards <span class="pl-k">=</span> num_unit_shards</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._num_proj_shards <span class="pl-k">=</span> num_proj_shards</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._forget_bias <span class="pl-k">=</span> forget_bias</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">=</span> state_is_tuple</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._activation <span class="pl-k">=</span> activation <span class="pl-k">or</span> math_ops.tanh</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> num_proj:</td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._state_size <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">          LSTMStateTuple(num_units, num_proj)</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> state_is_tuple <span class="pl-k">else</span> num_units <span class="pl-k">+</span> num_proj)</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._output_size <span class="pl-k">=</span> num_proj</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._state_size <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">          LSTMStateTuple(num_units, num_units)</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> state_is_tuple <span class="pl-k">else</span> <span class="pl-c1">2</span> <span class="pl-k">*</span> num_units)</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._output_size <span class="pl-k">=</span> num_units</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._state_size</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._output_size</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>):</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run one step of LSTM.</span></td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      inputs: input Tensor, 2D, batch x num_units.</span></td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state: if `state_is_tuple` is False, this must be a state Tensor,</span></td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `2-D, batch x state_size`.  If `state_is_tuple` is True, this must be a</span></td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        tuple of state Tensors, both `2-D`, with column sizes `c_state` and</span></td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `m_state`.</span></td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Returns:</span></td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      A tuple containing:</span></td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - A `2-D, [batch x output_dim]`, Tensor representing the output of the</span></td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        LSTM after reading `inputs` when previous state was `state`.</span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Here output_dim is:</span></td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           num_proj if num_proj was set,</span></td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           num_units otherwise.</span></td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      - Tensor(s) representing the new state of LSTM after reading `inputs` when</span></td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the previous state was `state`.  Same type and shape(s) as `state`.</span></td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Raises:</span></td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      ValueError: If input size cannot be inferred from inputs via</span></td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        static shape inference.</span></td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">    num_proj <span class="pl-k">=</span> <span class="pl-c1">self</span>._num_units <span class="pl-k">if</span> <span class="pl-c1">self</span>._num_proj <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">else</span> <span class="pl-c1">self</span>._num_proj</td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">    sigmoid <span class="pl-k">=</span> math_ops.sigmoid</td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">      (c_prev, m_prev) <span class="pl-k">=</span> state</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">      c_prev <span class="pl-k">=</span> array_ops.slice(state, [<span class="pl-c1">0</span>, <span class="pl-c1">0</span>], [<span class="pl-k">-</span><span class="pl-c1">1</span>, <span class="pl-c1">self</span>._num_units])</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">      m_prev <span class="pl-k">=</span> array_ops.slice(state, [<span class="pl-c1">0</span>, <span class="pl-c1">self</span>._num_units], [<span class="pl-k">-</span><span class="pl-c1">1</span>, num_proj])</td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">    dtype <span class="pl-k">=</span> inputs.dtype</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">    input_size <span class="pl-k">=</span> inputs.get_shape().with_rank(<span class="pl-c1">2</span>)[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> input_size.value <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Could not infer input size from inputs.get_shape()[-1]<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">    scope <span class="pl-k">=</span> vs.get_variable_scope()</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> vs.variable_scope(scope, <span class="pl-v">initializer</span><span class="pl-k">=</span><span class="pl-c1">self</span>._initializer) <span class="pl-k">as</span> unit_scope:</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._num_unit_shards <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">        unit_scope.set_partitioner(</td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">            partitioned_variables.fixed_size_partitioner(</td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._num_unit_shards))</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">      <span class="pl-c"><span class="pl-c">#</span> i = input_gate, j = new_input, f = forget_gate, o = output_gate</span></td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">      lstm_matrix <span class="pl-k">=</span> _linear([inputs, m_prev], <span class="pl-c1">4</span> <span class="pl-k">*</span> <span class="pl-c1">self</span>._num_units, <span class="pl-v">bias</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">      i, j, f, o <span class="pl-k">=</span> array_ops.split(</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">          <span class="pl-v">value</span><span class="pl-k">=</span>lstm_matrix, <span class="pl-v">num_or_size_splits</span><span class="pl-k">=</span><span class="pl-c1">4</span>, <span class="pl-v">axis</span><span class="pl-k">=</span><span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">      <span class="pl-c"><span class="pl-c">#</span> Diagonal connections</span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._use_peepholes:</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> vs.variable_scope(unit_scope) <span class="pl-k">as</span> projection_scope:</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> <span class="pl-c1">self</span>._num_unit_shards <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">            projection_scope.set_partitioner(<span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">          w_f_diag <span class="pl-k">=</span> vs.get_variable(</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">              <span class="pl-s"><span class="pl-pds">&quot;</span>w_f_diag<span class="pl-pds">&quot;</span></span>, <span class="pl-v">shape</span><span class="pl-k">=</span>[<span class="pl-c1">self</span>._num_units], <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">          w_i_diag <span class="pl-k">=</span> vs.get_variable(</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">              <span class="pl-s"><span class="pl-pds">&quot;</span>w_i_diag<span class="pl-pds">&quot;</span></span>, <span class="pl-v">shape</span><span class="pl-k">=</span>[<span class="pl-c1">self</span>._num_units], <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">          w_o_diag <span class="pl-k">=</span> vs.get_variable(</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">              <span class="pl-s"><span class="pl-pds">&quot;</span>w_o_diag<span class="pl-pds">&quot;</span></span>, <span class="pl-v">shape</span><span class="pl-k">=</span>[<span class="pl-c1">self</span>._num_units], <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._use_peepholes:</td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">        c <span class="pl-k">=</span> (sigmoid(f <span class="pl-k">+</span> <span class="pl-c1">self</span>._forget_bias <span class="pl-k">+</span> w_f_diag <span class="pl-k">*</span> c_prev) <span class="pl-k">*</span> c_prev <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">             sigmoid(i <span class="pl-k">+</span> w_i_diag <span class="pl-k">*</span> c_prev) <span class="pl-k">*</span> <span class="pl-c1">self</span>._activation(j))</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">        c <span class="pl-k">=</span> (sigmoid(f <span class="pl-k">+</span> <span class="pl-c1">self</span>._forget_bias) <span class="pl-k">*</span> c_prev <span class="pl-k">+</span> sigmoid(i) <span class="pl-k">*</span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">             <span class="pl-c1">self</span>._activation(j))</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._cell_clip <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> pylint: disable=invalid-unary-operand-type</span></td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">        c <span class="pl-k">=</span> clip_ops.clip_by_value(c, <span class="pl-k">-</span><span class="pl-c1">self</span>._cell_clip, <span class="pl-c1">self</span>._cell_clip)</td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> pylint: enable=invalid-unary-operand-type</span></td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._use_peepholes:</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> sigmoid(o <span class="pl-k">+</span> w_o_diag <span class="pl-k">*</span> c) <span class="pl-k">*</span> <span class="pl-c1">self</span>._activation(c)</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">        m <span class="pl-k">=</span> sigmoid(o) <span class="pl-k">*</span> <span class="pl-c1">self</span>._activation(c)</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._num_proj <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">with</span> vs.variable_scope(<span class="pl-s"><span class="pl-pds">&quot;</span>projection<span class="pl-pds">&quot;</span></span>) <span class="pl-k">as</span> proj_scope:</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> <span class="pl-c1">self</span>._num_proj_shards <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">            proj_scope.set_partitioner(</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">                partitioned_variables.fixed_size_partitioner(</td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>._num_proj_shards))</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">          m <span class="pl-k">=</span> _linear(m, <span class="pl-c1">self</span>._num_proj, <span class="pl-v">bias</span><span class="pl-k">=</span><span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>._proj_clip <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">          <span class="pl-c"><span class="pl-c">#</span> pylint: disable=invalid-unary-operand-type</span></td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">          m <span class="pl-k">=</span> clip_ops.clip_by_value(m, <span class="pl-k">-</span><span class="pl-c1">self</span>._proj_clip, <span class="pl-c1">self</span>._proj_clip)</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">          <span class="pl-c"><span class="pl-c">#</span> pylint: enable=invalid-unary-operand-type</span></td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">    new_state <span class="pl-k">=</span> (LSTMStateTuple(c, m) <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">                 array_ops.concat([c, m], <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> m, new_state</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_enumerated_map_structure</span>(<span class="pl-smi">map_fn</span>, <span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">  ix <span class="pl-k">=</span> [<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">enumerated_fn</span>(<span class="pl-k">*</span><span class="pl-smi">inner_args</span>, <span class="pl-k">**</span><span class="pl-smi">inner_kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">    r <span class="pl-k">=</span> map_fn(ix[<span class="pl-c1">0</span>], <span class="pl-k">*</span>inner_args, <span class="pl-k">**</span>inner_kwargs)</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">    ix[<span class="pl-c1">0</span>] <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> r</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">return</span> nest.map_structure(enumerated_fn, <span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">DropoutWrapper</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Operator adding dropout to inputs and outputs of the given cell.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cell</span>, <span class="pl-smi">input_keep_prob</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>, <span class="pl-smi">output_keep_prob</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>,</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">state_keep_prob</span><span class="pl-k">=</span><span class="pl-c1">1.0</span>, <span class="pl-smi">variational_recurrent</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">               <span class="pl-smi">input_size</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">dtype</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">seed</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create a cell with added input, state, and/or output dropout.</span></td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    If `variational_recurrent` is set to `True` (**NOT** the default behavior),</span></td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    then the same dropout mask is applied at every step, as described in:</span></td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Y. Gal, Z Ghahramani.  &quot;A Theoretically Grounded Application of Dropout in</span></td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Recurrent Neural Networks&quot;.  https://arxiv.org/abs/1512.05287</span></td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Otherwise a different dropout mask is applied at every time step.</span></td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cell: an RNNCell, a projection to output_size is added to it.</span></td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      input_keep_prob: unit Tensor or float between 0 and 1, input keep</span></td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        probability; if it is constant and 1, no input dropout will be added.</span></td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      output_keep_prob: unit Tensor or float between 0 and 1, output keep</span></td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        probability; if it is constant and 1, no output dropout will be added.</span></td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state_keep_prob: unit Tensor or float between 0 and 1, output keep</span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        probability; if it is constant and 1, no output dropout will be added.</span></td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        State dropout is performed on the *output* states of the cell.</span></td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      variational_recurrent: Python bool.  If `True`, then the same</span></td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        dropout pattern is applied across all time steps per run call.</span></td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If this parameter is set, `input_size` **must** be provided.</span></td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      input_size: (optional) (possibly nested tuple of) `TensorShape` objects</span></td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        containing the depth(s) of the input tensors expected to be passed in to</span></td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        the `DropoutWrapper`.  Required and used **iff**</span></td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         `variational_recurrent = True` and `input_keep_prob &lt; 1`.</span></td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      dtype: (optional) The `dtype` of the input, state, and output tensors.</span></td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Required and used **iff** `variational_recurrent = True`.</span></td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      seed: (optional) integer, the randomness seed.</span></td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Raises:</span></td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      TypeError: if cell is not an RNNCell.</span></td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      ValueError: if any of the keep_probs are not between 0 and 1.</span></td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> _like_rnncell(cell):</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>The parameter cell is not a RNNCell.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-s"><span class="pl-pds">&quot;</span>DropoutWrapperInit<span class="pl-pds">&quot;</span></span>):</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">def</span> <span class="pl-en">tensor_and_const_value</span>(<span class="pl-smi">v</span>):</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">        tensor_value <span class="pl-k">=</span> ops.convert_to_tensor(v)</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">        const_value <span class="pl-k">=</span> tensor_util.constant_value(tensor_value)</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> (tensor_value, const_value)</td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">for</span> prob, attr <span class="pl-k">in</span> [(input_keep_prob, <span class="pl-s"><span class="pl-pds">&quot;</span>input_keep_prob<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">                         (state_keep_prob, <span class="pl-s"><span class="pl-pds">&quot;</span>state_keep_prob<span class="pl-pds">&quot;</span></span>),</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">                         (output_keep_prob, <span class="pl-s"><span class="pl-pds">&quot;</span>output_keep_prob<span class="pl-pds">&quot;</span></span>)]:</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">        tensor_prob, const_prob <span class="pl-k">=</span> tensor_and_const_value(prob)</td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> const_prob <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> const_prob <span class="pl-k">&lt;</span> <span class="pl-c1">0</span> <span class="pl-k">or</span> const_prob <span class="pl-k">&gt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Parameter <span class="pl-c1">%s</span> must be between 0 and 1: <span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">                             <span class="pl-k">%</span> (attr, const_prob))</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">          <span class="pl-c1">setattr</span>(<span class="pl-c1">self</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> attr, <span class="pl-c1">float</span>(const_prob))</td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">          <span class="pl-c1">setattr</span>(<span class="pl-c1">self</span>, <span class="pl-s"><span class="pl-pds">&quot;</span>_<span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> attr, tensor_prob)</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Set cell, variational_recurrent, seed before running the code below</span></td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell <span class="pl-k">=</span> cell</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._variational_recurrent <span class="pl-k">=</span> variational_recurrent</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._seed <span class="pl-k">=</span> seed</td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._recurrent_input_noise <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._recurrent_state_noise <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._recurrent_output_noise <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> variational_recurrent:</td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> dtype <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>When variational_recurrent=True, dtype must be provided<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">def</span> <span class="pl-en">convert_to_batch_shape</span>(<span class="pl-smi">s</span>):</td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Prepend a 1 for the batch dimension; for recurrent</span></td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> variational dropout we use the same dropout mask for all</span></td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> batch elements.</span></td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> array_ops.concat(</td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">            ([<span class="pl-c1">1</span>], tensor_shape.TensorShape(s).as_list()), <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">def</span> <span class="pl-en">batch_noise</span>(<span class="pl-smi">s</span>, <span class="pl-smi">inner_seed</span>):</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">        shape <span class="pl-k">=</span> convert_to_batch_shape(s)</td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> random_ops.random_uniform(shape, <span class="pl-v">seed</span><span class="pl-k">=</span>inner_seed, <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> (<span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(<span class="pl-c1">self</span>._input_keep_prob, numbers.Real) <span class="pl-k">or</span></td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">          <span class="pl-c1">self</span>._input_keep_prob <span class="pl-k">&lt;</span> <span class="pl-c1">1.0</span>):</td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> input_size <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">              <span class="pl-s"><span class="pl-pds">&quot;</span>When variational_recurrent=True and input_keep_prob &lt; 1.0 or <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">              <span class="pl-s"><span class="pl-pds">&quot;</span>is unknown, input_size must be provided<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._recurrent_input_noise <span class="pl-k">=</span> _enumerated_map_structure(</td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">lambda</span> <span class="pl-smi">i</span>, <span class="pl-smi">s</span>: batch_noise(s, <span class="pl-v">inner_seed</span><span class="pl-k">=</span><span class="pl-c1">self</span>._gen_seed(<span class="pl-s"><span class="pl-pds">&quot;</span>input<span class="pl-pds">&quot;</span></span>, i)),</td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">            input_size)</td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._recurrent_state_noise <span class="pl-k">=</span> _enumerated_map_structure(</td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">lambda</span> <span class="pl-smi">i</span>, <span class="pl-smi">s</span>: batch_noise(s, <span class="pl-v">inner_seed</span><span class="pl-k">=</span><span class="pl-c1">self</span>._gen_seed(<span class="pl-s"><span class="pl-pds">&quot;</span>state<span class="pl-pds">&quot;</span></span>, i)),</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">          cell.state_size)</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">      <span class="pl-c1">self</span>._recurrent_output_noise <span class="pl-k">=</span> _enumerated_map_structure(</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">lambda</span> <span class="pl-smi">i</span>, <span class="pl-smi">s</span>: batch_noise(s, <span class="pl-v">inner_seed</span><span class="pl-k">=</span><span class="pl-c1">self</span>._gen_seed(<span class="pl-s"><span class="pl-pds">&quot;</span>output<span class="pl-pds">&quot;</span></span>, i)),</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">          cell.output_size)</td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">_gen_seed</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">salt_prefix</span>, <span class="pl-smi">index</span>):</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._seed <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">    salt <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>_<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (salt_prefix, index)</td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">    string <span class="pl-k">=</span> (<span class="pl-c1">str</span>(<span class="pl-c1">self</span>._seed) <span class="pl-k">+</span> salt).encode(<span class="pl-s"><span class="pl-pds">&quot;</span>utf-8<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">int</span>(hashlib.md5(string).hexdigest()[:<span class="pl-c1">8</span>], <span class="pl-c1">16</span>) <span class="pl-k">&amp;</span> <span class="pl-c1"><span class="pl-k">0x</span>7FFFFFFF</span></td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.state_size</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.output_size</td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">zero_state</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-c1">type</span>(<span class="pl-c1">self</span>).<span class="pl-c1">__name__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZeroState<span class="pl-pds">&quot;</span></span>, <span class="pl-v">values</span><span class="pl-k">=</span>[batch_size]):</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.zero_state(batch_size, dtype)</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">_variational_recurrent_dropout_value</span>(</td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">      <span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">index</span>, <span class="pl-smi">value</span>, <span class="pl-smi">noise</span>, <span class="pl-smi">keep_prob</span>):</td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Performs dropout given the pre-calculated noise tensor.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> uniform [keep_prob, 1.0 + keep_prob)</span></td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">    random_tensor <span class="pl-k">=</span> keep_prob <span class="pl-k">+</span> noise</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> 0. if [keep_prob, 1.0) and 1. if [1.0, 1.0 + keep_prob)</span></td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">    binary_tensor <span class="pl-k">=</span> math_ops.floor(random_tensor)</td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">    ret <span class="pl-k">=</span> math_ops.div(value, keep_prob) <span class="pl-k">*</span> binary_tensor</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">    ret.set_shape(value.get_shape())</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> ret</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">_dropout</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">values</span>, <span class="pl-smi">salt_prefix</span>, <span class="pl-smi">recurrent_noise</span>, <span class="pl-smi">keep_prob</span>):</td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Decides whether to perform standard dropout or recurrent dropout.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>._variational_recurrent:</td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">def</span> <span class="pl-en">dropout</span>(<span class="pl-smi">i</span>, <span class="pl-smi">v</span>):</td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> nn_ops.dropout(</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">            v, <span class="pl-v">keep_prob</span><span class="pl-k">=</span>keep_prob, <span class="pl-v">seed</span><span class="pl-k">=</span><span class="pl-c1">self</span>._gen_seed(salt_prefix, i))</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> _enumerated_map_structure(dropout, values)</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">def</span> <span class="pl-en">dropout</span>(<span class="pl-smi">i</span>, <span class="pl-smi">v</span>, <span class="pl-smi">n</span>):</td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>._variational_recurrent_dropout_value(i, v, n, keep_prob)</td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> _enumerated_map_structure(dropout, values, recurrent_noise)</td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__call__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>, <span class="pl-smi">scope</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run the cell with the declared dropouts.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_should_dropout</span>(<span class="pl-smi">p</span>):</td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> (<span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(p, <span class="pl-c1">float</span>)) <span class="pl-k">or</span> p <span class="pl-k">&lt;</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> _should_dropout(<span class="pl-c1">self</span>._input_keep_prob):</td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">      inputs <span class="pl-k">=</span> <span class="pl-c1">self</span>._dropout(inputs, <span class="pl-s"><span class="pl-pds">&quot;</span>input<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">                             <span class="pl-c1">self</span>._recurrent_input_noise,</td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">                             <span class="pl-c1">self</span>._input_keep_prob)</td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">    output, new_state <span class="pl-k">=</span> <span class="pl-c1">self</span>._cell(inputs, state, scope)</td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> _should_dropout(<span class="pl-c1">self</span>._state_keep_prob):</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">      new_state <span class="pl-k">=</span> <span class="pl-c1">self</span>._dropout(new_state, <span class="pl-s"><span class="pl-pds">&quot;</span>state<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">                                <span class="pl-c1">self</span>._recurrent_state_noise,</td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">                                <span class="pl-c1">self</span>._state_keep_prob)</td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> _should_dropout(<span class="pl-c1">self</span>._output_keep_prob):</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">      output <span class="pl-k">=</span> <span class="pl-c1">self</span>._dropout(output, <span class="pl-s"><span class="pl-pds">&quot;</span>output<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">                             <span class="pl-c1">self</span>._recurrent_output_noise,</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">                             <span class="pl-c1">self</span>._output_keep_prob)</td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> output, new_state</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ResidualWrapper</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>RNNCell wrapper that ensures cell inputs are added to the outputs.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cell</span>):</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Constructs a `ResidualWrapper` for `cell`.</span></td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cell: An instance of `RNNCell`.</span></td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell <span class="pl-k">=</span> cell</td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.state_size</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.output_size</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">zero_state</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-c1">type</span>(<span class="pl-c1">self</span>).<span class="pl-c1">__name__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZeroState<span class="pl-pds">&quot;</span></span>, <span class="pl-v">values</span><span class="pl-k">=</span>[batch_size]):</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.zero_state(batch_size, dtype)</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__call__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>, <span class="pl-smi">scope</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run the cell and add its inputs to its outputs.</span></td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      inputs: cell inputs.</span></td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state: cell state.</span></td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      scope: optional cell scope.</span></td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Returns:</span></td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      Tuple of cell outputs and new state.</span></td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Raises:</span></td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      TypeError: If cell inputs and outputs have different structure (type).</span></td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      ValueError: If cell inputs and outputs have different structure (value).</span></td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">    outputs, new_state <span class="pl-k">=</span> <span class="pl-c1">self</span>._cell(inputs, state, <span class="pl-v">scope</span><span class="pl-k">=</span>scope)</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">    nest.assert_same_structure(inputs, outputs)</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span> Ensure shapes match</span></td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">assert_shape_match</span>(<span class="pl-smi">inp</span>, <span class="pl-smi">out</span>):</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">      inp.get_shape().assert_is_compatible_with(out.get_shape())</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">    nest.map_structure(assert_shape_match, inputs, outputs)</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">    res_outputs <span class="pl-k">=</span> nest.map_structure(</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">lambda</span> <span class="pl-smi">inp</span>, <span class="pl-smi">out</span>: inp <span class="pl-k">+</span> out, inputs, outputs)</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> (res_outputs, new_state)</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">DeviceWrapper</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Operator that ensures an RNNCell runs on a particular device.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cell</span>, <span class="pl-smi">device</span>):</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Construct a `DeviceWrapper` for `cell` with device `device`.</span></td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Ensures the wrapped `cell` is called with `tf.device(device)`.</span></td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cell: An instance of `RNNCell`.</span></td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      device: A device string or function, for passing to `tf.device`.</span></td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell <span class="pl-k">=</span> cell</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._device <span class="pl-k">=</span> device</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.state_size</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.output_size</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">zero_state</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-c1">type</span>(<span class="pl-c1">self</span>).<span class="pl-c1">__name__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZeroState<span class="pl-pds">&quot;</span></span>, <span class="pl-v">values</span><span class="pl-k">=</span>[batch_size]):</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">with</span> ops.device(<span class="pl-c1">self</span>._device):</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell.zero_state(batch_size, dtype)</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__call__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>, <span class="pl-smi">scope</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run the cell on specified device.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.device(<span class="pl-c1">self</span>._device):</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">self</span>._cell(inputs, state, <span class="pl-v">scope</span><span class="pl-k">=</span>scope)</td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">MultiRNNCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>RNN cell composed sequentially of multiple simple cells.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cells</span>, <span class="pl-smi">state_is_tuple</span><span class="pl-k">=</span><span class="pl-c1">True</span>):</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create a RNN cell composed sequentially of a number of RNNCells.</span></td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cells: list of RNNCells that will be composed in this order.</span></td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      state_is_tuple: If True, accepted and returned states are n-tuples, where</span></td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        `n = len(cells)`.  If False, the states are all</span></td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        concatenated along the column axis.  This latter behavior will soon be</span></td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        deprecated.</span></td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Raises:</span></td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      ValueError: if cells is empty (not allowed), or at least one of the cells</span></td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        returns a state tuple but the flag `state_is_tuple` is `False`.</span></td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">super</span>(MultiRNNCell, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>()</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> cells:</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Must specify at least one cell for MultiRNNCell.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> nest.is_sequence(cells):</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span>(</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">          <span class="pl-s"><span class="pl-pds">&quot;</span>cells must be a list or tuple, but saw: <span class="pl-c1">%s</span>.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> cells)</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cells <span class="pl-k">=</span> cells</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">=</span> state_is_tuple</td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">any</span>(nest.is_sequence(c.state_size) <span class="pl-k">for</span> c <span class="pl-k">in</span> <span class="pl-c1">self</span>._cells):</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Some cells return tuples of states, but the flag <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span>state_is_tuple is not set.  State sizes are: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">                         <span class="pl-k">%</span> <span class="pl-c1">str</span>([c.state_size <span class="pl-k">for</span> c <span class="pl-k">in</span> <span class="pl-c1">self</span>._cells]))</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">tuple</span>(cell.state_size <span class="pl-k">for</span> cell <span class="pl-k">in</span> <span class="pl-c1">self</span>._cells)</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> <span class="pl-c1">sum</span>([cell.state_size <span class="pl-k">for</span> cell <span class="pl-k">in</span> <span class="pl-c1">self</span>._cells])</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._cells[<span class="pl-k">-</span><span class="pl-c1">1</span>].output_size</td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">zero_state</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">batch_size</span>, <span class="pl-smi">dtype</span>):</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> ops.name_scope(<span class="pl-c1">type</span>(<span class="pl-c1">self</span>).<span class="pl-c1">__name__</span> <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>ZeroState<span class="pl-pds">&quot;</span></span>, <span class="pl-v">values</span><span class="pl-k">=</span>[batch_size]):</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">tuple</span>(cell.zero_state(batch_size, dtype) <span class="pl-k">for</span> cell <span class="pl-k">in</span> <span class="pl-c1">self</span>._cells)</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> We know here that state_size of each cell is not a tuple and</span></td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> presumably does not contain TensorArrays or anything else fancy</span></td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">super</span>(MultiRNNCell, <span class="pl-c1">self</span>).zero_state(batch_size, dtype)</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>):</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Run this multi-layer cell on inputs, starting from state.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line">    cur_state_pos <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line">    cur_inp <span class="pl-k">=</span> inputs</td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">    new_states <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">for</span> i, cell <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">self</span>._cells):</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">with</span> vs.variable_scope(<span class="pl-s"><span class="pl-pds">&quot;</span>cell_<span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> i):</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple:</td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">          <span class="pl-k">if</span> <span class="pl-k">not</span> nest.is_sequence(state):</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>Expected state to be a tuple of length <span class="pl-c1">%d</span>, but received: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">                (<span class="pl-c1">len</span>(<span class="pl-c1">self</span>.state_size), state))</td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">          cur_state <span class="pl-k">=</span> state[i]</td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">          cur_state <span class="pl-k">=</span> array_ops.slice(state, [<span class="pl-c1">0</span>, cur_state_pos],</td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">                                      [<span class="pl-k">-</span><span class="pl-c1">1</span>, cell.state_size])</td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">          cur_state_pos <span class="pl-k">+=</span> cell.state_size</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">        cur_inp, new_state <span class="pl-k">=</span> cell(cur_inp, cur_state)</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">        new_states.append(new_state)</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">    new_states <span class="pl-k">=</span> (<span class="pl-c1">tuple</span>(new_states) <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_is_tuple <span class="pl-k">else</span></td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">                  array_ops.concat(new_states, <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> cur_inp, new_states</td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">_SlimRNNCell</span>(<span class="pl-e">RNNCell</span>):</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>A simple wrapper for slim.rnn_cells.<span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">cell_fn</span>):</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Create a SlimRNNCell from a cell_fn.</span></td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Args:</span></td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      cell_fn: a function which takes (inputs, state, scope) and produces the</span></td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        outputs and the new_state. Additionally when called with inputs=None and</span></td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        state=None it should return (initial_outputs, initial_state).</span></td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Raises:</span></td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      TypeError: if cell_fn is not callable</span></td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      ValueError: if cell_fn cannot produce a valid initial state.</span></td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">callable</span>(cell_fn):</td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">TypeError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>cell_fn <span class="pl-c1">%s</span> needs to be callable<span class="pl-pds">&quot;</span></span>, cell_fn)</td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell_fn <span class="pl-k">=</span> cell_fn</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._cell_name <span class="pl-k">=</span> cell_fn.func.<span class="pl-c1">__name__</span></td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">    init_output, init_state <span class="pl-k">=</span> <span class="pl-c1">self</span>._cell_fn(<span class="pl-c1">None</span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">    output_shape <span class="pl-k">=</span> init_output.get_shape()</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">    state_shape <span class="pl-k">=</span> init_state.get_shape()</td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._output_size <span class="pl-k">=</span> output_shape.with_rank(<span class="pl-c1">2</span>)[<span class="pl-c1">1</span>].value</td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">self</span>._state_size <span class="pl-k">=</span> state_shape.with_rank(<span class="pl-c1">2</span>)[<span class="pl-c1">1</span>].value</td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._output_size <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Initial output created by <span class="pl-c1">%s</span> has invalid shape <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line">                       (<span class="pl-c1">self</span>._cell_name, output_shape))</td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">self</span>._state_size <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Initial state created by <span class="pl-c1">%s</span> has invalid shape <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span></td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line">                       (<span class="pl-c1">self</span>._cell_name, state_shape))</td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">state_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._state_size</td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line">  <span class="pl-en">@</span><span class="pl-c1">property</span></td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-en">output_size</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-c1">self</span>._output_size</td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">def</span> <span class="pl-c1">__call__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">inputs</span>, <span class="pl-smi">state</span>, <span class="pl-smi">scope</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line">    scope <span class="pl-k">=</span> scope <span class="pl-k">or</span> <span class="pl-c1">self</span>._cell_name</td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line">    output, state <span class="pl-k">=</span> <span class="pl-c1">self</span>._cell_fn(inputs, state, <span class="pl-v">scope</span><span class="pl-k">=</span>scope)</td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> output, state</td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">_linear</span>(<span class="pl-smi">args</span>,</td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">output_size</span>,</td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">bias</span>,</td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">bias_initializer</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line">            <span class="pl-smi">kernel_initializer</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line">  <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span>Linear map: sum_i(args[i] * W[i]), where W[i] is a variable.</span></td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Args:</span></td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    args: a 2D Tensor or a list of 2D, batch x n, Tensors.</span></td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    output_size: int, second dimension of W[i].</span></td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    bias: boolean, whether to add a bias term or not.</span></td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    bias_initializer: starting value to initialize the bias</span></td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line"><span class="pl-s">      (default is all zeros).</span></td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    kernel_initializer: starting value to initialize the weight.</span></td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Returns:</span></td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    A 2D Tensor with shape [batch x output_size] equal to</span></td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    sum_i(args[i] * W[i]), where W[i]s are newly created matrices.</span></td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  Raises:</span></td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    ValueError: if some of the arguments has unspecified or wrong shape.</span></td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line"><span class="pl-s">  <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> args <span class="pl-k">is</span> <span class="pl-c1">None</span> <span class="pl-k">or</span> (nest.is_sequence(args) <span class="pl-k">and</span> <span class="pl-k">not</span> args):</td>
      </tr>
      <tr>
        <td id="L1015" class="blob-num js-line-number" data-line-number="1015"></td>
        <td id="LC1015" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>`args` must be specified<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1016" class="blob-num js-line-number" data-line-number="1016"></td>
        <td id="LC1016" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">if</span> <span class="pl-k">not</span> nest.is_sequence(args):</td>
      </tr>
      <tr>
        <td id="L1017" class="blob-num js-line-number" data-line-number="1017"></td>
        <td id="LC1017" class="blob-code blob-code-inner js-file-line">    args <span class="pl-k">=</span> [args]</td>
      </tr>
      <tr>
        <td id="L1018" class="blob-num js-line-number" data-line-number="1018"></td>
        <td id="LC1018" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1019" class="blob-num js-line-number" data-line-number="1019"></td>
        <td id="LC1019" class="blob-code blob-code-inner js-file-line">  <span class="pl-c"><span class="pl-c">#</span> Calculate the total size of arguments on dimension 1.</span></td>
      </tr>
      <tr>
        <td id="L1020" class="blob-num js-line-number" data-line-number="1020"></td>
        <td id="LC1020" class="blob-code blob-code-inner js-file-line">  total_arg_size <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1021" class="blob-num js-line-number" data-line-number="1021"></td>
        <td id="LC1021" class="blob-code blob-code-inner js-file-line">  shapes <span class="pl-k">=</span> [a.get_shape() <span class="pl-k">for</span> a <span class="pl-k">in</span> args]</td>
      </tr>
      <tr>
        <td id="L1022" class="blob-num js-line-number" data-line-number="1022"></td>
        <td id="LC1022" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">for</span> shape <span class="pl-k">in</span> shapes:</td>
      </tr>
      <tr>
        <td id="L1023" class="blob-num js-line-number" data-line-number="1023"></td>
        <td id="LC1023" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> shape.ndims <span class="pl-k">!=</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="L1024" class="blob-num js-line-number" data-line-number="1024"></td>
        <td id="LC1024" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>linear is expecting 2D arguments: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> shapes)</td>
      </tr>
      <tr>
        <td id="L1025" class="blob-num js-line-number" data-line-number="1025"></td>
        <td id="LC1025" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> shape[<span class="pl-c1">1</span>].value <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1026" class="blob-num js-line-number" data-line-number="1026"></td>
        <td id="LC1026" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">raise</span> <span class="pl-c1">ValueError</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>linear expects shape[1] to be provided for shape <span class="pl-c1">%s</span>, <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1027" class="blob-num js-line-number" data-line-number="1027"></td>
        <td id="LC1027" class="blob-code blob-code-inner js-file-line">                       <span class="pl-s"><span class="pl-pds">&quot;</span>but saw <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (shape, shape[<span class="pl-c1">1</span>]))</td>
      </tr>
      <tr>
        <td id="L1028" class="blob-num js-line-number" data-line-number="1028"></td>
        <td id="LC1028" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1029" class="blob-num js-line-number" data-line-number="1029"></td>
        <td id="LC1029" class="blob-code blob-code-inner js-file-line">      total_arg_size <span class="pl-k">+=</span> shape[<span class="pl-c1">1</span>].value</td>
      </tr>
      <tr>
        <td id="L1030" class="blob-num js-line-number" data-line-number="1030"></td>
        <td id="LC1030" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1031" class="blob-num js-line-number" data-line-number="1031"></td>
        <td id="LC1031" class="blob-code blob-code-inner js-file-line">  dtype <span class="pl-k">=</span> [a.dtype <span class="pl-k">for</span> a <span class="pl-k">in</span> args][<span class="pl-c1">0</span>]</td>
      </tr>
      <tr>
        <td id="L1032" class="blob-num js-line-number" data-line-number="1032"></td>
        <td id="LC1032" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1033" class="blob-num js-line-number" data-line-number="1033"></td>
        <td id="LC1033" class="blob-code blob-code-inner js-file-line">  <span class="pl-c"><span class="pl-c">#</span> Now the computation.</span></td>
      </tr>
      <tr>
        <td id="L1034" class="blob-num js-line-number" data-line-number="1034"></td>
        <td id="LC1034" class="blob-code blob-code-inner js-file-line">  scope <span class="pl-k">=</span> vs.get_variable_scope()</td>
      </tr>
      <tr>
        <td id="L1035" class="blob-num js-line-number" data-line-number="1035"></td>
        <td id="LC1035" class="blob-code blob-code-inner js-file-line">  <span class="pl-k">with</span> vs.variable_scope(scope) <span class="pl-k">as</span> outer_scope:</td>
      </tr>
      <tr>
        <td id="L1036" class="blob-num js-line-number" data-line-number="1036"></td>
        <td id="LC1036" class="blob-code blob-code-inner js-file-line">    weights <span class="pl-k">=</span> vs.get_variable(</td>
      </tr>
      <tr>
        <td id="L1037" class="blob-num js-line-number" data-line-number="1037"></td>
        <td id="LC1037" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">_WEIGHTS_VARIABLE_NAME</span>, [total_arg_size, output_size],</td>
      </tr>
      <tr>
        <td id="L1038" class="blob-num js-line-number" data-line-number="1038"></td>
        <td id="LC1038" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype,</td>
      </tr>
      <tr>
        <td id="L1039" class="blob-num js-line-number" data-line-number="1039"></td>
        <td id="LC1039" class="blob-code blob-code-inner js-file-line">        <span class="pl-v">initializer</span><span class="pl-k">=</span>kernel_initializer)</td>
      </tr>
      <tr>
        <td id="L1040" class="blob-num js-line-number" data-line-number="1040"></td>
        <td id="LC1040" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-c1">len</span>(args) <span class="pl-k">==</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L1041" class="blob-num js-line-number" data-line-number="1041"></td>
        <td id="LC1041" class="blob-code blob-code-inner js-file-line">      res <span class="pl-k">=</span> math_ops.matmul(args[<span class="pl-c1">0</span>], weights)</td>
      </tr>
      <tr>
        <td id="L1042" class="blob-num js-line-number" data-line-number="1042"></td>
        <td id="LC1042" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1043" class="blob-num js-line-number" data-line-number="1043"></td>
        <td id="LC1043" class="blob-code blob-code-inner js-file-line">      res <span class="pl-k">=</span> math_ops.matmul(array_ops.concat(args, <span class="pl-c1">1</span>), weights)</td>
      </tr>
      <tr>
        <td id="L1044" class="blob-num js-line-number" data-line-number="1044"></td>
        <td id="LC1044" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> <span class="pl-k">not</span> bias:</td>
      </tr>
      <tr>
        <td id="L1045" class="blob-num js-line-number" data-line-number="1045"></td>
        <td id="LC1045" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">return</span> res</td>
      </tr>
      <tr>
        <td id="L1046" class="blob-num js-line-number" data-line-number="1046"></td>
        <td id="LC1046" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">with</span> vs.variable_scope(outer_scope) <span class="pl-k">as</span> inner_scope:</td>
      </tr>
      <tr>
        <td id="L1047" class="blob-num js-line-number" data-line-number="1047"></td>
        <td id="LC1047" class="blob-code blob-code-inner js-file-line">      inner_scope.set_partitioner(<span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L1048" class="blob-num js-line-number" data-line-number="1048"></td>
        <td id="LC1048" class="blob-code blob-code-inner js-file-line">      <span class="pl-k">if</span> bias_initializer <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1049" class="blob-num js-line-number" data-line-number="1049"></td>
        <td id="LC1049" class="blob-code blob-code-inner js-file-line">        bias_initializer <span class="pl-k">=</span> init_ops.constant_initializer(<span class="pl-c1">0.0</span>, <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype)</td>
      </tr>
      <tr>
        <td id="L1050" class="blob-num js-line-number" data-line-number="1050"></td>
        <td id="LC1050" class="blob-code blob-code-inner js-file-line">      biases <span class="pl-k">=</span> vs.get_variable(</td>
      </tr>
      <tr>
        <td id="L1051" class="blob-num js-line-number" data-line-number="1051"></td>
        <td id="LC1051" class="blob-code blob-code-inner js-file-line">          <span class="pl-c1">_BIAS_VARIABLE_NAME</span>, [output_size],</td>
      </tr>
      <tr>
        <td id="L1052" class="blob-num js-line-number" data-line-number="1052"></td>
        <td id="LC1052" class="blob-code blob-code-inner js-file-line">          <span class="pl-v">dtype</span><span class="pl-k">=</span>dtype,</td>
      </tr>
      <tr>
        <td id="L1053" class="blob-num js-line-number" data-line-number="1053"></td>
        <td id="LC1053" class="blob-code blob-code-inner js-file-line">          <span class="pl-v">initializer</span><span class="pl-k">=</span>bias_initializer)</td>
      </tr>
      <tr>
        <td id="L1054" class="blob-num js-line-number" data-line-number="1054"></td>
        <td id="LC1054" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> nn_ops.bias_add(res, biases)</td>
      </tr>
</table>

  <div class="BlobToolbar position-absolute js-file-line-actions dropdown js-menu-container js-select-menu d-none" aria-hidden="true">
    <button class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1 dropdown-toggle js-menu-target" id="js-file-line-action-button" type="button" aria-expanded="false" aria-haspopup="true" aria-label="Inline file action toolbar" aria-controls="inline-file-actions">
      <svg aria-hidden="true" class="octicon" height="16" version="1.1" viewBox="0 0 13 4" width="14">
        <g stroke="none" stroke-width="1" fill-rule="evenodd">
            <g transform="translate(-1.000000, -6.000000)">
                <path d="M2.5,9.5 C1.67157288,9.5 1,8.82842712 1,8 C1,7.17157288 1.67157288,6.5 2.5,6.5 C3.32842712,6.5 4,7.17157288 4,8 C4,8.82842712 3.32842712,9.5 2.5,9.5 Z M7.5,9.5 C6.67157288,9.5 6,8.82842712 6,8 C6,7.17157288 6.67157288,6.5 7.5,6.5 C8.32842712,6.5 9,7.17157288 9,8 C9,8.82842712 8.32842712,9.5 7.5,9.5 Z M12.5,9.5 C11.6715729,9.5 11,8.82842712 11,8 C11,7.17157288 11.6715729,6.5 12.5,6.5 C13.3284271,6.5 14,7.17157288 14,8 C14,8.82842712 13.3284271,9.5 12.5,9.5 Z"></path>
            </g>
        </g>
      </svg>
    </button>
    <div class="dropdown-menu-content js-menu-content" id="inline-file-actions">
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2">
        <li><a class="js-zeroclipboard dropdown-item" style="cursor:pointer;" id="js-copy-lines" data-original-text="Copy lines">Copy lines</a></li>
        <li><a class="js-zeroclipboard dropdown-item" id= "js-copy-permalink" style="cursor:pointer;" data-original-text="Copy permalink">Copy permalink</a></li>
          <li><a href="/tensorflow/tensorflow/issues/new" class="dropdown-item" id="js-new-issue">Open new issue</a></li>
      </ul>
    </div>
  </div>

  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>

  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2017 <span title="0.16290s from unicorn-379352754-9kpzb">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-91f98c37fc84eac24836eec2567e9912742094369a04c4eba6e3cd1fa18902d9.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-45273a0ef5972dc44bf2be3423f94af39640500abcbb2c35f11d2621913ef70f.js"></script>
    
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-f38268493cdd5fff2f7769c291386812f6d5167a88b7dd8e6414c1e717e90165.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

