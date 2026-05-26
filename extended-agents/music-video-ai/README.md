# Music Video AI Division

AI-native music video production is not just "generate cool shots to a song." It is a timecoded pipeline with section maps, hook moments, performance continuity, render routing, and rhythm-aware editorial conform.

This division turns that workflow into specialized agents that can take a project from track intent and timecode structure through shotboards, seed images, motion prompts, lyric-performance planning, render dispatch, and final cut review.

## Pipeline Map

1. Track bible and intent lock
2. Section and hook timecode mapping
3. Performance continuity and look locks
4. Visual motif and shotboard planning
5. Seed-image prompt packaging
6. Lyric and performance gesture planning
7. WAN and LTX2 motion prompt compilation
8. Render routing and dispatch
9. Rhythm conform, assembly, and final QA

## Core Artifact Chain

| Phase | Primary Artifacts | Purpose |
|---|---|---|
| Track | `Track_Bible.md`, `Track_Source_Brief.json`, `Motif_Registry.md` | Defines song intent, source, mood, and recurring visual strategy |
| Structure | `Section_Map.json`, `Hook_Moments.json`, `Timecode_Grid.json` | Maps intros, verses, choruses, bridges, drops, and key sync moments |
| Continuity | `Performance_Lookbook.json`, `Look_Lock_Registry.md`, `Set_State_Map.json` | Keeps performer identity, wardrobe, props, and location state stable |
| Visual Planning | `Visual_Motif_Plan.md`, `Shotboard.json`, `Coverage_Plan.md` | Converts sections into coverage and section-specific visual logic |
| Image Prep | `Seed_Image_List.json`, `Keyframe_Prompts.json` | Creates prompt-safe anchor images and conditioning inputs |
| Performance | `Lyric_Performance_Map.json`, `LipSync_Risk_Map.json`, `Gesture_Cue_Sheet.json` | Aligns lyrics, performance intent, gesture, and sync risk to timecode |
| Motion | `Motion_Clip_Cards.json`, `WAN_I2V_Pack.json`, `LTX2_Prompts.json` | Model-ready motion prompts and clip definitions |
| Editorial | `Render_Manifest.json`, `Edit_Conform_Map.json`, `QC_Report.md` | Queue control, cut order, trims, and readiness decisions |

## Timecode and Performance Chain

Music-video pipelines fail when shots are generated without respect for section timing. Use this chain:

1. `Section_Map.json`
   - One row per intro, verse, pre-chorus, chorus, bridge, drop, solo, or outro.
   - Fields: `section_id`, `start_sec`, `end_sec`, `energy`, `lyric_range`, `visual_mode`.
2. `Hook_Moments.json`
   - One row per beat, lyric punch, glance, gesture, flash cut, or drop hit that should drive the cut.
   - Fields: `hook_id`, `time_sec`, `trigger_type`, `priority`, `editorial_action`.
3. `Lyric_Performance_Map.json`
   - One row per lyric phrase or performance moment.
   - Fields: `section_id`, `phrase_id`, `start_sec`, `end_sec`, `delivery_mode`, `gesture`, `camera_priority`, `sync_risk`.
4. `Gesture_Cue_Sheet.json`
   - Maps body action, prop interaction, and glance timing to sections and hooks.
5. `Edit_Conform_Map.json`
   - Declares clip in/out, transition type, beat alignment, and allowable drift against the track.

Rules:
- Hook moments outrank generic coverage.
- Performance identity is a continuity lock, not a styling suggestion.
- Lyric-led shots and atmosphere-led shots should be labeled differently.
- Every render batch should know whether it serves performance, motif, transition, or texture.

## Agent Roster

| Agent | Role | Status |
|---|---|---|
| Music Video AI Orchestrator | Runs the end-to-end music-video pipeline | Implemented |
| Music Video Track Bible Architect | Locks track intent, motifs, and source constraints | Implemented |
| Music Video Structure & Timecode Mapper | Maps sections, hooks, and sync-critical moments | Implemented |
| Music Video Performance Continuity Director | Maintains look locks, set states, and performer continuity | Implemented |
| Music Video Visual Motif Planner | Defines section-level visual language and recurrence | Implemented |
| Music Video Shotboard Director | Builds board-ready coverage and frame plans by section | Implemented |
| Music Video Seed Image Prompt Engineer | Produces keyframes and seed images for generation | Implemented |
| Music Video WAN I2V Director | Controls image-conditioned motion for performance shots | Implemented |
| Music Video Motion Reference Director | Routes choreography, path, and gesture references | Implemented |
| Music Video LTX2 Prompt Compiler | Compiles clip cards and LTX2/WAN motion prompts | Implemented |
| Music Video Lyric Performance Planner | Maps lyric delivery, lip-sync, and gesture to timecode | Implemented |
| Music Video Model Router & Render Dispatcher | Routes jobs across models, profiles, and retry paths | Implemented |
| Music Video Rhythm Edit Conformer | Builds the cut against the track and section grid | Implemented |
| Music Video Continuity Reality Checker | Final skeptical QA for sync, continuity, and edit readiness | Implemented |

## Recommended Activation Order

1. Music Video Track Bible Architect
2. Music Video Structure & Timecode Mapper
3. Music Video Performance Continuity Director
4. Music Video Visual Motif Planner
5. Music Video Shotboard Director
6. Music Video Seed Image Prompt Engineer
7. Music Video WAN I2V Director and Music Video Motion Reference Director
8. Music Video LTX2 Prompt Compiler
9. Music Video Lyric Performance Planner
10. Music Video Model Router & Render Dispatcher
11. Music Video Rhythm Edit Conformer
12. Music Video Continuity Reality Checker
13. Music Video AI Orchestrator for gate control and delivery readiness

## Design Principles

- Track structure before visual volume.
- Hook moments before ornamental coverage.
- Performance continuity before style drift.
- Model syntax should never replace editorial timing.
- Every artifact should be reusable without replaying the whole track analysis.
