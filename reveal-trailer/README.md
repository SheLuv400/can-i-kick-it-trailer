# CAN I KICK IT — Reveal trailer assembly

Editable 90-second, 1920×1080, 30 fps Remotion project. Seven independently editable scenes, plus a complete timeline.

## Current delivery

This is a SILENT EDITORIAL ASSEMBLY, not the completed official trailer. The supplied artist art, official logo, Suno music, DJ Kickit WAV and game SFX were not present. No character faces, card designs, gameplay or game UI have been invented. Artist names and the end title are temporary typography. Generated arena/CRT/crate images are cinematic background plates with camera animation; they are not game footage or fully animated character cinematics. The crate shot is a glowing open-crate concept plate; an animated opening and real mystery-card reveal still need production. The DJ is represented by the booth and record imagery, not an animated performer.

## Start and export

Use this existing checkout; cloud tasks are already isolated, so no additional Git worktree is needed.

```sh
cd /workspace/can-i-kick-it-trailer/reveal-trailer
npm ci
npm run studio
npm run check
npm run render
```

The verified local browser is `/usr/bin/chromium`. In another environment, remove the explicit browser argument if using Remotion's managed browser. Studio's `Reveal` composition is 2700 frames. Each of the seven scene compositions is also independently renderable. `out/` contains the 90-second assembly and individual scene MP4s.

## Replace the reserved clips

Put files in `public/`, then set their relative paths in `src/assets.ts`. Examples: `battle: 'gameplay/battle.mp4'`, `logo: 'original/logo.png'`. Empty paths show editorial insert slates. Real gameplay is fitted without cropping; no fake health meters or UI overlays are added.

| Field | Global timeline | Required content |
|---|---|---|
| battle | 00:22–00:38 | 16 seconds: cards hit stage slots, abilities, HP and Crowd Meters, big attack |
| comeback | 00:42–00:54 | 12 seconds: mystery card, Backstage knockout, revival |
| menus | 01:00–01:08 | 8 seconds: Mixtape Studio, Ultimate Team, collection, deck building |
| finale | 01:08–01:18 | 10 seconds: low meters, Encore, silence, bass impact, victory |

Use 1080p footage at 30 fps or higher. Clips start at their first frame; trim the sources to the desired action before importing. Keep the footage's UI intact. The reserved clip windows total 46 seconds. The 00:54–01:00 section contains the three requested feature titles; menus follow them.

Original artwork fields `macko`, `cipher`, `amara`, `nikki`, `ziggy` accept PNG/JPG/WebP files (transparent PNG preferred); they fit without cropping. The original logo replaces the temporary end-title lettering. Artist names remain editable in `src/scenes/Artists.tsx`.

## Audio finishing

No replacement or synthetic DJ voice/music is included. `audio-cues.csv` lists the requested sound/voice timing. Original timing and pacing are provisional until the Suno tracks are available; this assembly is not yet beat-synced to them.

Place your files in `public/audio/`. Edit `audio-manifest.json` to match actual filenames, lengths and source offsets. `python3 mix-audio.py` mixes those stems into `public/audio/trailer-mix.wav`, with fades, music ducking beneath DJ voice and a limiter. Then set `soundtrack: 'audio/trailer-mix.wav'` in `src/assets.ts` and render again. Missing files cause the mixer to fail clearly rather than silently omitting a stem. Listen and adjust the source trims to the actual recordings before final delivery.

The script uses the original recordings; it does not synthesize missing dialogue or crowd chants. A voice file containing several lines must be cut with source offsets, or split into the named takes.

## Finishing checklist

- Replace all four editorial insert slates with actual captured footage.
- Supply original character art and official logo.
- Add and audition the existing music, DJ voice and game sound effects.
- Fine-cut transitions to the actual beats and action impacts.
- Check face/card fidelity, UI readability, audio balance and sync in the complete export.
- Render `Reveal` for a finished master. Never publish the assembly as actual gameplay.
