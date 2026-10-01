> For Mintlify product knowledge (components, configuration, writing standards),
> install the Mintlify skill: `npx skills add https://mintlify.com/docs`

# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- Use the Mintlify MCP server, `https://mcp.mintlify.com`, to edit content and settings via MCP
- Use the Mintlify docs MCP server, `https://www.mintlify.com/docs/mcp`, to query information about using Mintlify via MCP

## Terminology

- The product is **Superlog**. The open-source repository is `superloglabs/responder-oss`; use the name Responder only when referring to that repository or to identifiers in it.
- An **automation** has **triggers**, **agent instructions**, **repositories**, **connectors**, a **model**, and a **harness**. One execution is a **run**.
- **Tag mode** answers Slack mentions. It is separate from automations.
- Use "workspace" for the tenant and "integration" for a connected tool.
- Positioning follows the landing page at superlog.sh: automate routine engineering tasks; choose your model and harness; bring your own tokens and subscriptions.

## Style preferences

- Plain, direct language. Short sentences. No marketing flourish.
- Use active voice and second person ("you")
- Keep sentences concise — one idea per sentence
- Use sentence case for headings
- Bold for UI elements: Click **Settings**
- Code formatting for file names, commands, paths, and code references

## Content boundaries

- Document what the current code does. Check claims against `superloglabs/responder-oss` before publishing.
- Document the automations product that hosted workspaces get. Do not document internal admin features.
