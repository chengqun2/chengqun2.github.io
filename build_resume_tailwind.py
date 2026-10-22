# -*- coding: utf-8 -*-
"""Generate index.html & eng_resume.html — Tailwind CSS + Font Awesome.

Regenerate English project list from legacy:
  python scripts/extract_projects_en.py
"""
from __future__ import annotations

import html
from pathlib import Path


def parse_projects(path: Path) -> list[tuple[str, str, str]]:
    raw = path.read_text(encoding="utf-8")
    items: list[tuple[str, str, str]] = []
    for block in raw.split("\n---\n"):
        block = block.strip()
        if not block:
            continue
        lines = block.split("\n", 2)
        if len(lines) < 2:
            continue
        title = lines[0].strip().replace("&amp;", "&")
        time = lines[1].strip()
        desc = lines[2].strip() if len(lines) > 2 else ""
        items.append((title, time, desc))
    return items


def project_cards(items: list[tuple[str, str, str]]) -> str:
    parts: list[str] = []
    for i, (title, time, desc) in enumerate(items):
        delay = min(0.35 + i * 0.02, 0.9)
        d = html.escape(desc)[:1200]
        parts.append(
            f"""<article class="group rounded-xl border border-slate-200/90 bg-white/80 p-4 shadow-sm opacity-0 transition-all duration-300 animate-fade-rise hover:-translate-y-0.5 hover:border-indigo-200/80 hover:shadow-md" style="animation-delay:{delay}s">
  <div class="flex flex-wrap items-start justify-between gap-2 border-b border-slate-100 pb-2">
    <h3 class="text-base font-semibold text-slate-800 group-hover:text-indigo-700 transition-colors">{html.escape(title)}</h3>
    <time class="shrink-0 rounded-full bg-slate-100 px-3 py-0.5 text-xs font-medium text-slate-500 tabular-nums">{html.escape(time)}</time>
  </div>
  <p class="mt-3 text-sm leading-relaxed text-slate-600">{d}</p>
</article>"""
        )
    return "\n".join(parts)


HEAD_COMMON = """  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
          },
          colors: {
            ink: { 950: '#0f172a', 800: '#1e293b', 600: '#475569', 500: '#64748b' },
          },
          keyframes: {
            'fade-rise': {
              '0%': { opacity: '0', transform: 'translateY(10px)' },
              '100%': { opacity: '1', transform: 'translateY(0)' },
            },
          },
          animation: { 'fade-rise': 'fade-rise 0.55s ease-out forwards' },
        },
      },
    };
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" crossorigin="anonymous" />"""


def build_html(
    *,
    lang: str,
    title: str,
    name: str,
    role_line: str,
    meta_desc: str,
    other_link: str,
    other_label: str,
    hero_demographics: str,
    summary_inner: str,
    prefs_title: str,
    prefs_rows: list[tuple[str, str]],
    work_title: str,
    work_cards: str,
    projects_title: str,
    projects_grid: str,
    edu_title: str,
    edu_html: str,
    skills_title: str,
    skills_html: str,
) -> str:
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(meta_desc)}" />
{HEAD_COMMON}
  <style>
    @media (prefers-reduced-motion: reduce) {{
      .animate-fade-rise {{ animation: none !important; opacity: 1 !important; }}
    }}
    html {{ scroll-behavior: smooth; }}
  </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-slate-100 via-slate-50 to-indigo-50/40 font-sans text-slate-800 antialiased">
  <div class="pointer-events-none fixed inset-0 -z-10 bg-[radial-gradient(ellipse_80%_50%_at_50%_-20%,rgba(99,102,241,0.12),transparent)]"></div>

  <header class="relative overflow-hidden border-b border-white/60 bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-slate-100 shadow-lg shadow-indigo-950/20">
    <div class="absolute inset-0 bg-[url('data:image/svg+xml,%3Csvg width=\\'60\\' height=\\'60\\' viewBox=\\'0 0 60 60\\' xmlns=\\'http://www.w3.org/2000/svg\\'%3E%3Cg fill=\\'none\\' fill-rule=\\'evenodd\\'%3E%3Cg fill=\\'%23ffffff\\' fill-opacity=\\'0.04\\'%3E%3Cpath d=\\'M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z\\'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E')] opacity-80"></div>
    <div class="relative mx-auto max-w-4xl px-4 py-10 sm:px-6 sm:py-14">
      <div class="flex flex-col gap-8 md:flex-row md:items-center md:justify-between">
        <div class="flex flex-col items-center gap-6 sm:flex-row sm:items-start">
          <img src="https://avatars.githubusercontent.com/u/12636050" width="120" height="120" alt="{html.escape(name)}" class="h-28 w-28 rounded-2xl border-4 border-white/10 object-cover shadow-xl ring-2 ring-white/10 transition duration-300 hover:ring-indigo-300/50" />
          <div class="text-center sm:text-left">
            <p class="mb-1 text-xs font-semibold uppercase tracking-[0.2em] text-indigo-200/90">{html.escape(role_line)}</p>
            <h1 class="text-3xl font-bold tracking-tight text-white sm:text-4xl">{html.escape(name)}</h1>
            <div class="mt-4 flex flex-wrap justify-center gap-2 sm:justify-start">
              <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-500/15 px-3 py-1 text-xs font-semibold text-emerald-200 ring-1 ring-emerald-400/30"><i class="fa-brands fa-python"></i> Python</span>
              <span class="inline-flex items-center gap-1.5 rounded-full bg-sky-500/15 px-3 py-1 text-xs font-semibold text-sky-200 ring-1 ring-sky-400/30"><i class="fa-brands fa-react"></i> React</span>
              <span class="inline-flex items-center gap-1.5 rounded-full bg-violet-500/15 px-3 py-1 text-xs font-semibold text-violet-200 ring-1 ring-violet-400/30"><i class="fa-solid fa-wand-magic-sparkles"></i> Vibe coding</span>
            </div>
            <div class="mt-5 flex flex-wrap justify-center gap-3 sm:justify-start">
              <a href="{html.escape(other_link, quote=True)}" class="inline-flex items-center gap-2 rounded-full bg-white/10 px-4 py-2 text-sm font-medium text-white ring-1 ring-white/20 backdrop-blur transition hover:bg-white/20 hover:ring-white/40">
                <i class="fa-solid fa-language"></i> {html.escape(other_label)}
              </a>
              <a href="https://www.champcodeacademy.com/" target="_blank" rel="noopener noreferrer" class="print:hidden inline-flex items-center gap-2 rounded-full bg-indigo-500 px-4 py-2 text-sm font-semibold text-white shadow-lg shadow-indigo-600/30 transition hover:bg-indigo-400 hover:shadow-indigo-500/40">
                <i class="fa-solid fa-graduation-cap"></i> Champ Code Academy
              </a>
            </div>
          </div>
        </div>
        <div class="print:hidden mx-auto w-full max-w-[220px] shrink-0 md:mx-0">
          <video class="w-full rounded-xl border border-white/10 shadow-2xl ring-1 ring-white/10 transition hover:ring-indigo-400/30" controls preload="metadata">
            <source src="self_introduction.mp4" type="video/mp4" />
          </video>
          <p class="mt-2 text-center text-[11px] text-slate-400">{'Self-intro video' if lang == 'en' else '自我介绍视频'}</p>
        </div>
      </div>
      <ul class="mt-8 flex flex-wrap justify-center gap-x-6 gap-y-3 border-t border-white/10 pt-6 text-sm text-slate-300 sm:justify-start">
        {hero_demographics}
      </ul>
    </div>
  </header>

  <main class="mx-auto max-w-4xl space-y-8 px-4 py-10 [overflow-wrap:anywhere] sm:px-6 sm:py-12">

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.04s">
      <h2 class="mb-4 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-user-tie"></i></span>
        {'Professional Summary' if lang == 'en' else '职业概要'}
      </h2>
      <div class="space-y-4 text-sm leading-relaxed text-slate-600 [&_strong]:font-semibold [&_strong]:text-slate-800">
        {summary_inner}
      </div>
    </section>

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.08s">
      <h2 class="mb-4 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-bullseye"></i></span>
        {html.escape(prefs_title)}
      </h2>
      <dl class="grid gap-4 sm:grid-cols-2">
        {''.join(f'<div class="rounded-xl bg-slate-50/80 p-4 ring-1 ring-slate-100 transition hover:bg-indigo-50/50 hover:ring-indigo-100"><dt class="text-xs font-semibold uppercase tracking-wide text-slate-400">{html.escape(k)}</dt><dd class="mt-1 font-medium text-slate-800">{html.escape(v)}</dd></div>' for k, v in prefs_rows)}
      </dl>
    </section>

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.12s">
      <h2 class="mb-6 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-building"></i></span>
        {html.escape(work_title)}
      </h2>
      <div class="space-y-5">
        {work_cards}
      </div>
    </section>

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.16s">
      <h2 class="mb-6 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-diagram-project"></i></span>
        {html.escape(projects_title)}
      </h2>
      <div class="grid gap-4 sm:grid-cols-2">
        {projects_grid}
      </div>
    </section>

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.2s">
      <h2 class="mb-4 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-graduation-cap"></i></span>
        {html.escape(edu_title)}
      </h2>
      {edu_html}
    </section>

    <section class="animate-fade-rise rounded-2xl border border-slate-200/80 bg-white/90 p-6 opacity-0 shadow-sm backdrop-blur-sm transition-shadow duration-300 hover:shadow-md sm:p-8" style="animation-delay:0.24s">
      <h2 class="mb-4 flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-indigo-600">
        <span class="flex h-8 w-8 items-center justify-center rounded-lg bg-indigo-50 text-indigo-600"><i class="fa-solid fa-star"></i></span>
        {html.escape(skills_title)}
      </h2>
      {skills_html}
    </section>

    <p class="pb-8 text-center text-xs text-slate-400">© {html.escape(name)} · Resume</p>
  </main>
</body>
</html>
"""


def work_card(
    company: str,
    period: str,
    role: str,
    meta: str,
    body_html: str,
) -> str:
    return f"""<article class="rounded-xl border border-slate-200/90 bg-gradient-to-br from-white to-slate-50/80 p-5 shadow-sm transition-all duration-300 hover:border-indigo-200 hover:shadow-md">
  <div class="flex flex-wrap items-start justify-between gap-2">
    <div>
      <h3 class="text-lg font-semibold text-slate-900">{html.escape(company)}</h3>
      <p class="mt-0.5 text-sm text-indigo-600">{html.escape(role)}</p>
      <p class="mt-1 text-xs text-slate-500">{html.escape(meta)}</p>
    </div>
    <time class="shrink-0 rounded-lg bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600 tabular-nums">{html.escape(period)}</time>
  </div>
  <div class="mt-4 border-t border-slate-100 pt-4 text-sm leading-relaxed text-slate-600 [&_a]:text-indigo-600 [&_a:hover]:underline">{body_html}</div>
</article>"""


def main() -> None:
    root = Path(__file__).resolve().parent
    zh_sum = (root / "assets" / "resume-summary-zh.html").read_text(encoding="utf-8")
    en_sum = (root / "assets" / "resume-summary-en.html").read_text(encoding="utf-8")
    zh_proj = parse_projects(root / "_projects_zh.txt")
    en_proj = parse_projects(root / "_projects_en.txt")

    zh_jobs = [
        (
            "江苏方软科技有限公司",
            "2023/6 — 至今",
            "全栈开发（Python 后端 / React 前端）",
            "50–150 人 · 民营",
            "<div class='space-y-3'>"
            "<p><strong>Python 服务从 0 到 1 搭建：</strong>负责需求梳理与技术选型，基于 Python / Flask 初始化工程，划分路由、业务逻辑与数据访问模块，管理依赖和环境配置；完成数据结构与 REST API 设计、接口开发及 React 联调，再通过 Docker + Nginx 部署上线，持续进行日志排查与功能迭代。</p>"
            "<p><strong>Python 后端与 AI 应用：</strong>以 Python 为主要后端语言，负责内部系统接口、业务逻辑及智能化服务开发；对接 Dify、Ollama 与 DeepSeek-R1 等模型 API，支撑 RAG 知识库问答，并通过 n8n 串联大模型与内外业务系统。</p>"
            "<p><strong>数据处理与自动化：</strong>使用 Python 编写数据处理、接口集成和运维脚本，结合 MySQL、ClickHouse、ElasticSearch 完成数据读写与检索；配合 React 管理端交付完整业务功能。</p>"
            "<p><strong>云平台与部署运维：</strong>熟悉华为云、阿里云环境下的应用部署与维护，结合 Linux、Docker、Nginx 部署 Python 服务及相关中间件，开展环境配置、日志排查和日常运维；负责 Dify、n8n、Ollama 等服务的私有化部署与维护。</p>"
            "<p class='rounded-lg bg-emerald-50/70 px-3 py-2 text-emerald-900'><strong>Python 技术栈：</strong>Python · Flask · Requests · REST API / JSON · pandas · MySQL · Dify / Ollama API · Docker / Linux</p>"
            "</div>",
        ),
        (
            "上海维智卓新信息科技有限公司",
            "2022/7 — 2023/5（10 个月）",
            "全栈开发（Python 后端 / React 前端）",
            "150–500 人 · 民营",
            "<div class='space-y-3'>"
            "<p>面向新加坡少儿编程在线教育业务，<strong>全英文远程协作</strong>；<strong>独立从 0 到 1 交付</strong> <a class='text-indigo-600 font-medium hover:underline' href='https://www.champcodeacademy.com/' target='_blank' rel='noopener'>Champ Code Academy</a> 官网，以 <strong>Python + React</strong> 完成服务端接口、前端展示、部署及后续迭代。</p>"
            "<p><strong>Python 后端从 0 到 1 建设：</strong>从官网与 CRM 的业务需求出发，初始化 Flask 项目，搭建模块结构、路由与环境配置，设计数据交互和 REST API；编写业务接口并对接 Chargebee / Stripe 订阅计费与支付服务，完成 React 前后端联调、部署上线及上线后的问题跟进，形成从工程搭建到业务落地的完整交付流程。</p>"
            "<p><strong>Python 自动化与系统协作：</strong>编写数据同步及流程处理脚本，结合 Airtable、Make、n8n 衔接 CRM、计费和营销系统；配合 Supabase 数据服务与 Jira 完成需求交付和问题跟进。</p>"
            "<p class='rounded-lg bg-emerald-50/70 px-3 py-2 text-emerald-900'><strong>Python 技术栈：</strong>Python · Flask · Requests · REST API / JSON · Chargebee / Stripe API · Airtable API；前端 React</p>"
            "</div>",
        ),
        (
            "南京维数软件股份有限公司",
            "2017/12 — 2022/7（4 年 7 个月）",
            "全栈开发（前后端）",
            "上市 · 150–500 人",
            "<p>研发部：市公安局及分局 <strong>办公 OA、车辆大数据、综合指挥、感知大数据</strong> 等；Java 后台为主，需求与库表设计与核心模块。</p><p>Spring Cloud/Boot、Kafka、Hadoop/HBase、Solr 等高数据量场景。</p>",
        ),
        (
            "优因信息科技有限公司",
            "2015/7 — 2017/12（2 年 5 个月）",
            "全栈开发（前后端）",
            "50–150 人 · 民营",
            "<p>需求对接、后台架构与数据库设计、接口开发，<strong>项目管理</strong>。</p>",
        ),
        (
            "江苏华生恒业科技股份有限公司",
            "2011/9 — 2015/7（3 年 10 个月）",
            "全栈开发（前后端）",
            "500–1000 人 · 民营",
            "<p>Java B/S 开发与维护；人才公共服务网、台玻 ERP、国家电网 OA、微信服务号后台等。</p>",
        ),
    ]
    en_jobs = [
        (
            "Jiangsu Fangruan Technology Co., Ltd.",
            "2023/6 — Present",
            "Full Stack Developer (Python Backend / React Frontend)",
            "50–150 employees · Private",
            "<div class='space-y-3'>"
            "<p><strong>Python services built from scratch:</strong> Own the process from requirements analysis and technology selection to production. Initialize Python / Flask projects, organize routing, business logic, and data access modules, and manage dependencies and environment configuration. Design data structures and REST APIs, implement endpoints, integrate with React, and deploy through Docker + Nginx, followed by log troubleshooting and ongoing iterations.</p>"
            "<p><strong>Python backend &amp; AI applications:</strong> Use Python as the primary backend language to develop internal APIs, business logic, and AI services. Integrate Dify, Ollama, and model APIs such as DeepSeek-R1 to support RAG knowledge-base Q&amp;A, with n8n connecting LLMs to internal and external business systems.</p>"
            "<p><strong>Data processing &amp; automation:</strong> Write Python scripts for data processing, API integration, and operational tasks. Work with MySQL, ClickHouse, and Elasticsearch for data access and retrieval, and deliver complete business features alongside React admin interfaces.</p>"
            "<p><strong>Cloud deployment &amp; operations:</strong> Familiar with deploying and maintaining applications on Huawei Cloud and Alibaba Cloud. Use Linux, Docker, and Nginx to deploy Python services and middleware, configure environments, troubleshoot logs, and handle routine operations. Deploy and maintain self-hosted Dify, n8n, and Ollama services.</p>"
            "<p class='rounded-lg bg-emerald-50/70 px-3 py-2 text-emerald-900'><strong>Python stack:</strong> Python · Flask · Requests · REST APIs / JSON · pandas · MySQL · Dify / Ollama APIs · Docker / Linux</p>"
            "</div>",
        ),
        (
            "Shanghai Wayz Intelligence Information Technology Co., Ltd.",
            "2022/7 — 2023/5 (10 mo)",
            "Full Stack Developer (Python Backend / React Frontend)",
            "150–500 employees · Private",
            "<div class='space-y-3'>"
            "<p>Supported a Singapore-based children's coding education business through <strong>fully remote collaboration in English</strong>. <strong>Independently delivered from scratch to production</strong> the <a class='text-indigo-600 font-medium hover:underline' href='https://www.champcodeacademy.com/' target='_blank' rel='noopener'>Champ Code Academy</a> website using <strong>Python + React</strong>, covering backend APIs, frontend pages, deployment, and subsequent iterations.</p>"
            "<p><strong>Python backend built from scratch:</strong> Translated website and CRM requirements into a Flask project, setting up the module structure, routing, and environment configuration, then designing data interactions and REST APIs. Implemented business endpoints and Chargebee / Stripe subscription billing and payment integrations, completed integration with the React frontend, deployed the application, and resolved post-launch issues, covering the full process from project setup to business delivery.</p>"
            "<p><strong>Python automation &amp; system integration:</strong> Wrote data synchronization and workflow-processing scripts, connecting CRM, billing, and marketing systems through Airtable, Make, and n8n. Worked with Supabase data services and used Jira for delivery and issue tracking.</p>"
            "<p class='rounded-lg bg-emerald-50/70 px-3 py-2 text-emerald-900'><strong>Python stack:</strong> Python · Flask · Requests · REST APIs / JSON · Chargebee / Stripe APIs · Airtable API; React frontend</p>"
            "</div>",
        ),
        (
            "Nanjing Weishu Software Co., Ltd.",
            "2017/12 — 2022/7 (4y7m)",
            "Full Stack Developer",
            "Listed · 150–500 employees",
            "<p>Developed <strong>office automation, vehicle big data, integrated command, and sensor data platforms</strong> for municipal and district public security bureaus. Focused on Java backend development, requirements analysis, database design, and core modules.</p><p>Worked with Spring Cloud / Spring Boot, Kafka, Hadoop / HBase, and Solr in high-volume data systems.</p>",
        ),
        (
            "Youyin Information Technology Co., Ltd.",
            "2015/7 — 2017/12 (2y5m)",
            "Full Stack Developer",
            "50–150 employees · Private",
            "<p>Handled requirements coordination, backend architecture, database design, API development, and <strong>project management</strong>.</p>",
        ),
        (
            "Jiangsu Huasheng Hengye Technology Co., Ltd.",
            "2011/9 — 2015/7 (3y10m)",
            "Full Stack Developer",
            "500–1000 employees · Private",
            "<p>Developed and maintained Java web applications, including a public talent services portal, Taiwan Glass ERP, State Grid office automation, and WeChat service-account backends.</p>",
        ),
    ]

    zh_work_html = "\n".join(work_card(*j) for j in zh_jobs)
    en_work_html = "\n".join(work_card(*j) for j in en_jobs)

    zh_prefs = [
        ("期望职位", "全栈（Python / React）"),
        ("期望城市", "远程 (Remote)"),
        ("期望月薪", "面议"),
        ("工作类型", "全职"),
        ("求职状态", "在职，寻求好的机会"),
        ("到岗时间", "2 周内"),
    ]
    en_prefs = [
        ("Position", "Full Stack (Python / React)"),
        ("Location", "Remote"),
        ("Expected Salary", "Negotiable"),
        ("Job Type", "Full-time"),
        ("Status", "Employed, open to opportunities"),
        ("Availability", "Within 2 weeks"),
    ]

    edu_zh = """<div class="flex flex-col gap-4 rounded-xl border border-slate-100 bg-slate-50/50 p-4 sm:flex-row sm:items-center">
  <img src="https://img01.51jobcdn.com/im/school/%25E6%2589%25AC%25E5%25B7%259E%25E5%25A4%25A7%25E5%25AD%25A6%25E5%25B9%25BF%25E9%2599%25B5%25E5%25AD%25A6%25E9%2599%25A2.jpg" width="56" height="56" alt="" class="h-14 w-14 rounded-lg object-cover ring-1 ring-slate-200" />
  <div>
    <p class="font-semibold text-slate-900">扬州大学广陵学院</p>
    <p class="text-sm text-slate-600">本科 · 计算机科学与技术</p>
    <p class="mt-1 text-xs text-slate-500 tabular-nums">2007/9 — 2011/7</p>
  </div>
</div>"""
    edu_en = edu_zh.replace("扬州大学广陵学院", "Guangling College, Yangzhou University").replace(
        "本科 · 计算机科学与技术", "Bachelor's degree · Computer Science and Technology"
    )

    skills_zh = """<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1.5 text-xs font-bold text-emerald-900 ring-2 ring-emerald-300/70"><i class="fa-brands fa-python"></i> Python · 熟练</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1.5 text-xs font-bold text-emerald-900 ring-2 ring-emerald-300/70">Flask / Requests / pandas</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-indigo-50 px-3 py-1.5 text-xs font-bold text-indigo-900 ring-2 ring-indigo-300/70"><i class="fa-solid fa-cloud"></i> 华为云 · 熟悉</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-indigo-50 px-3 py-1.5 text-xs font-bold text-indigo-900 ring-2 ring-indigo-300/70"><i class="fa-solid fa-cloud"></i> 阿里云 · 熟悉</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-orange-50 px-3 py-1.5 text-xs font-bold text-orange-900 ring-2 ring-orange-300/70"><i class="fa-brands fa-java"></i> Java · 熟练</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-lime-50 px-3 py-1.5 text-xs font-bold text-lime-900 ring-2 ring-lime-300/70"><i class="fa-brands fa-node-js"></i> Node.js · 熟练</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-sky-50 px-3 py-1.5 text-xs font-bold text-sky-900 ring-2 ring-sky-300/70"><i class="fa-brands fa-react"></i> React · 熟练</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-teal-50 px-3 py-1.5 text-xs font-bold text-teal-900 ring-2 ring-teal-300/70"><i class="fa-brands fa-vuejs"></i> Vue · 熟练</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-amber-50 px-3 py-1.5 text-xs font-bold text-amber-900 ring-2 ring-amber-300/70"><i class="fa-solid fa-language"></i> 英语 · 熟练</span>
</div>"""
    skills_en = """<div class="flex flex-wrap gap-2">
  <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1.5 text-xs font-bold text-emerald-900 ring-2 ring-emerald-300/70"><i class="fa-brands fa-python"></i> Python · Proficient</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-3 py-1.5 text-xs font-bold text-emerald-900 ring-2 ring-emerald-300/70">Flask / Requests / pandas</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-indigo-50 px-3 py-1.5 text-xs font-bold text-indigo-900 ring-2 ring-indigo-300/70"><i class="fa-solid fa-cloud"></i> Huawei Cloud · Familiar</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-indigo-50 px-3 py-1.5 text-xs font-bold text-indigo-900 ring-2 ring-indigo-300/70"><i class="fa-solid fa-cloud"></i> Alibaba Cloud · Familiar</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-orange-50 px-3 py-1.5 text-xs font-bold text-orange-900 ring-2 ring-orange-300/70"><i class="fa-brands fa-java"></i> Java · Proficient</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-lime-50 px-3 py-1.5 text-xs font-bold text-lime-900 ring-2 ring-lime-300/70"><i class="fa-brands fa-node-js"></i> Node.js · Proficient</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-sky-50 px-3 py-1.5 text-xs font-bold text-sky-900 ring-2 ring-sky-300/70"><i class="fa-brands fa-react"></i> React · Proficient</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-teal-50 px-3 py-1.5 text-xs font-bold text-teal-900 ring-2 ring-teal-300/70"><i class="fa-brands fa-vuejs"></i> Vue · Proficient</span>
  <span class="inline-flex items-center gap-1.5 rounded-full bg-amber-50 px-3 py-1.5 text-xs font-bold text-amber-900 ring-2 ring-amber-300/70"><i class="fa-solid fa-language"></i> English · Proficient</span>
</div>"""

    hero_zh = """<li class="flex items-center gap-2"><i class="fa-solid fa-mars text-slate-400"></i> 男 · 1989/09</li>
        <li class="flex items-center gap-2"><i class="fa-solid fa-briefcase text-indigo-300"></i> 近15年工作经验</li>
        <li class="flex items-center gap-2"><i class="fa-solid fa-location-dot text-rose-300"></i> 江苏盐城</li>"""
    hero_en = """<li class="flex items-center gap-2"><i class="fa-solid fa-mars text-slate-400"></i> Male · 1989/09</li>
        <li class="flex items-center gap-2"><i class="fa-solid fa-briefcase text-indigo-300"></i> Nearly 15 years of experience</li>
        <li class="flex items-center gap-2"><i class="fa-solid fa-location-dot text-rose-300"></i> Yancheng, Jiangsu, China</li>"""

    index_html = build_html(
        lang="zh-CN",
        title="成群 — 全栈开发 · 在线简历",
        name="成群",
        role_line="Full Stack · Python / React",
        meta_desc="近15年全栈开发，重点 Python 后端、Flask、API 集成与自动化；React 全栈交付，熟悉华为云、阿里云部署运维，具备 AI 大模型应用及新加坡全英文远程经验。",
        other_link="eng_resume.html",
        other_label="English resume",
        hero_demographics=hero_zh + """
        <li><a href="tel:18662062998" class="flex items-center gap-2 transition hover:text-white"><i class="fa-solid fa-phone text-emerald-300"></i> 18662062998</a></li>
        <li><a href="mailto:chengqun710@163.com" class="flex items-center gap-2 transition hover:text-white"><i class="fa-solid fa-envelope text-amber-300"></i> chengqun710@163.com</a></li>""",
        summary_inner=zh_sum,
        prefs_title="求职意向",
        prefs_rows=zh_prefs,
        work_title="工作经验",
        work_cards=zh_work_html,
        projects_title="项目经验",
        projects_grid=project_cards(zh_proj),
        edu_title="教育经历",
        edu_html=edu_zh,
        skills_title="技能特长",
        skills_html=skills_zh,
    )
    eng_html = build_html(
        lang="en",
        title="Chengqun — Full Stack (Python / React) · Resume",
        name="Chengqun",
        role_line="Full Stack · Python / React",
        meta_desc="Nearly 15 years of full-stack development, focused on Python backends, Flask, API integrations, and automation. React delivery; familiar with Huawei Cloud and Alibaba Cloud deployment and operations; AI/LLM applications and English-speaking remote collaboration with Singapore teams.",
        other_link="index.html",
        other_label="中文简历",
        hero_demographics=hero_en + """
        <li><a href="tel:18662062998" class="flex items-center gap-2 transition hover:text-white"><i class="fa-solid fa-phone text-emerald-300"></i> 18662062998</a></li>
        <li><a href="mailto:chengqun710@163.com" class="flex items-center gap-2 transition hover:text-white"><i class="fa-solid fa-envelope text-amber-300"></i> chengqun710@163.com</a></li>""",
        summary_inner=en_sum,
        prefs_title="Job Preferences",
        prefs_rows=en_prefs,
        work_title="Work Experience",
        work_cards=en_work_html,
        projects_title="Project Experience",
        projects_grid=project_cards(en_proj),
        edu_title="Education",
        edu_html=edu_en,
        skills_title="Skills",
        skills_html=skills_en,
    )

    (root / "index.html").write_text(index_html, encoding="utf-8")
    (root / "eng_resume.html").write_text(eng_html, encoding="utf-8")
    print("Wrote index.html, eng_resume.html")


if __name__ == "__main__":
    main()
