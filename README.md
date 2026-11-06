# CAN I KICK IT — THE GAME

90-second reveal trailer **editorial assembly**, rendered at 1920×1080, 30 fps.

## Downloads

Open a link below to download the file. If GitHub shows a file page instead, use **Download raw file**.

- [Trailer MP4 — 69 MB](https://github.com/SheLuv400/can-i-kick-it-trailer/raw/refs/heads/main/downloads/can-i-kick-it-90s-assembly.mp4)
- [Seven individual scenes — ZIP, 59 MB](https://github.com/SheLuv400/can-i-kick-it-trailer/raw/refs/heads/main/downloads/individual-scenes.zip)
- [Editable Remotion project — ZIP, 6 MB](https://github.com/SheLuv400/can-i-kick-it-trailer/raw/refs/heads/main/downloads/editable-project.zip)

## What is included

- Seven independently editable scenes on the requested 90-second timeline.
- Generated arena, CRT booth and record-crate background plates, animated camera moves, titles, vinyl and microphone graphics.
- Four clearly marked replacement windows for actual gameplay and menus.
- Source project, audio cue sheet and a helper for mixing supplied recordings.

**This is a silent work-in-progress assembly, not the finished official trailer.** Original artist artwork, official logo, Suno music, DJ Kickit WAV, game sound effects and actual gameplay were not available during production. Artist names and end-title lettering are temporary. The background plates are cinematic concepts, not game footage. No character faces, card designs or game UI were invented.

## Editing

See [the project instructions](reveal-trailer/README.md) for setup, asset replacement and audio finishing.

```sh
cd reveal-trailer
npm ci
npm run studio
```

The complete composition is `Reveal`. Change asset paths in `src/assets.ts`. The render command uses `/usr/bin/chromium`, as verified in the cloud environment; adjust that path for another machine.

## Validation

The complete master was verified as H.264, exactly 90 seconds, 1920×1080, 30 fps, 2,700 frames. A full decode completed without errors. All seven exported scene clips passed their expected duration and frame-count checks.
