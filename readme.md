# MSIT Parallel Code Reviews 🚀

Hi! 👋 Schön, dass du da bist. Dieses Repository nutzen wir als gemeinsamen, kollaborativen Workspace.

---

## 🎯 Warum machen wir das?
Wir wollen lernen, sauberes und hilfreiches Feedback zu geben, fremden Code besser zu verstehen und natürlich fleißig Nerd-Punkte 🤓 zu sammeln!

---

## 🛠️ Der Workflow

### 1. Eigenen Code reviewen lassen
* **Up to date bleiben:** Wechsle auf den `main`-Branch und ziehe den neuesten Stand (`git pull origin main`).
* **Branch erstellen:** Erstelle einen eigenen Feature-Branch mit einem eindeutigen Namen (z. B. `git switch -c mein-feature`).
* **Ordner nutzen:** Erstelle im Ordner `code_reviews` einen Unterordner mit deinem Namen oder Projekttitel und lege dort deinen Code ab.
* **Code pushen:** Lade deinen Branch auf GitHub hoch (`git push -u origin mein-feature`).
* **Pull Request (PR) erstellen:** Gehe auf GitHub und öffne einen PR von deinem Branch in den `main`-Branch.
* **Reviewer einladen:** Füge rechts in der Seitenleiste unter *Assignees* oder *Reviewers* deine Teammitglieder hinzu oder sag einfach im Chat Bescheid.

### 2. Fremden Code reviewen (2 Wege)

#### Weg A: Direkt auf GitHub (Im Browser)
1. Öffne den entsprechenden Pull Request auf GitHub.
2. Gehe auf den Reiter **"Files changed"**.
3. Bewege die Maus über eine Codezeile, klicke auf das **`+` Icon** und schreibe direkt deinen Kommentar.

#### Weg B: Direkt in VS Code (Empfohlen)
1. Installiere die Erweiterung: [GitHub Pull Requests and Issues](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github).
2. Klicke auf das neue GitHub-Icon in deiner VS Code Seitenleiste und melde dich an.
3. Aktualisiere deine lokale Version deines Repos mit allen neuen remote Branches: `git fetch`
4. Nun hast du Links in der Leiste ein neues Icon und siehst alle offenen PRs und kannst Code direkt in der IDE kommentieren, ohne die Website zu öffnen.
