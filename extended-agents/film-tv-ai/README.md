# Film & TV AI Division

AI-native film and television development is not a single prompt. It is a production pipeline with durable artifacts, continuity locks, model-routing decisions, and editorial QA.

This division turns that pipeline into specialized agents that can take a project from theme and canon through screenplay, visual beats, seed images, motion prompts, renders, audio planning, and final assembly.

## Pipeline Map

1. Theme and canon lock
2. Screenplay expansion and bridge scene insertion
3. Scene-card and visual-beat decomposition
4. Character continuity and seed-image prompt packaging
5. Motion prompt compilation for WAN and LTX2
6. Dialogue, ambience, foley, score, and voice planning
7. Render dispatch, stitch order, and QC
8. Final assembly and delivery

## Core Artifact Chain

| Phase | Primary Artifacts | Purpose |
|---|---|---|
| Theme | `Theme_Bible.md`, `Canon_Lock_Registry.md`, `Character_DB.json` | Narrative north star, immutable truths, identity locks |
| Screenplay | `Phase1_Script_Screenplay.md`, `Phase2_Complete_Screenplay.md`, `Phase2_Scene_Structure.json` | Numbered scenes, bridge/injection logic, continuity-aware scene structure |
| Visual Design | `Phase3_Visual_Beats.json`, `Scene_Cards.json`, `Beat_Summary.md` | Shot-friendly beat breakdown with blocking, lighting, wardrobe, and sound cues |
| Image Prep | `Seed_Image_Prompts.json`, `Episode_Image_List.json` | Character-stable keyframes and prompt packaging |
| Motion Prep | `WAN_Clips.json`, `Phase4_LTXV2_Prompts.json`, `Clip_Cards.json` | Model-ready motion prompts with durations, continuity locks, and editing intent |
| Audio | `Dialogue_Timing.json`, `Voice_Casting.json`, `Audio_Beat_Map.json`, `ADR_TTS_Map.json` | Dialogue, performance, ambience, foley, score, and sync handoff |
| Editorial | `Stitch_Order.md`, `Final_Assembly_Guide.md`, `Render_Manifest.json`, `QC_Report.md` | Assembly sequencing, manifests, and quality gates |

## Audio and Dialogue Artifact Chain

The visual pipeline is already strong in most AI film workflows. The missing piece is usually audio discipline. Use this chain:

1. `Dialogue_Timing.json`
   - One row per spoken line.
   - Fields: `scene_id`, `beat_id`, `line_id`, `speaker`, `text`, `duration_sec`, `performance_intent`, `interruptible`, `sync_mode`.
2. `Voice_Casting.json`
   - One row per voice role.
   - Fields: `character_id`, `voice_id`, `age_band`, `accent`, `tone`, `reference_notes`, `fallback_voice_id`.
3. `Audio_Beat_Map.json`
   - One row per beat.
   - Fields: `scene_id`, `beat_id`, `ambient`, `foley`, `music_cue`, `silence_strategy`, `priority_sound`, `mix_notes`.
4. `ADR_TTS_Map.json`
   - One row per generated line or replacement.
   - Fields: `line_id`, `source`, `take_id`, `replace_reason`, `target_duration_sec`, `pickup_window_sec`, `delivery_status`.
5. `LipSync_QA.md`
   - Approval checklist for timing drift, emotional mismatch, mouth-shape plausibility, and overlap cleanup.

Rules:
- Story-critical information should never exist only in music or ambience.
- Dialogue timing belongs to beats, not only to scenes.
- Voice identity is a continuity lock, not an afterthought.
- Every render pass should know whether it is silent, ambience-first, dialogue-first, or music-led.

## Agent Roster

Implemented now:

| Agent | Role | Status |
|---|---|---|
| Film & TV AI Orchestrator | Runs the end-to-end AI film pipeline | Implemented |
| Film & TV Theme Bible Architect | Builds theme bible, canon locks, and character DB | Implemented |
| Film & TV Screenplay Expander | Expands canon into numbered screenplay and scene structure | Implemented |
| Film & TV Visual Beat Planner | Converts screenplay into visual-beat and scene-card artifacts | Implemented |
| Film & TV Seed Image Prompt Engineer | Builds seed-image and keyframe prompt packages | Implemented |
| Film & TV LTX2 Prompt Compiler | Compiles visual beats into WAN/LTX2 motion prompt packages | Implemented |
| Film & TV Dialogue & Audio Beat Planner | Creates dialogue, voice, ambience, foley, and sync artifacts | Implemented |
| Film & TV Character Continuity Director | Maintains look locks, costume states, props, injuries, and lifecycle changes | Implemented |
| Film & TV Storyboard Director | Turns beats into board-ready coverage packs and editorial frame plans | Implemented |
| Film & TV WAN I2V Director | Optimizes image-to-video generation and continuity-safe motion prompting | Implemented |
| Film & TV Motion Reference Director | Handles pose, path, and choreography reference routing | Implemented |
| Film & TV Model Router & Render Dispatcher | Routes jobs by model, memory profile, queue state, and retry class | Implemented |
| Film & TV Stitch Editor | Owns clip sequence, transition logic, trims, and final pacing | Implemented |
| Film & TV Continuity Reality Checker | Final skeptical QA for identity drift, shot resets, sync errors, and editorial breakage | Implemented |

## Recommended Activation Order

1. Film & TV Theme Bible Architect
2. Film & TV Screenplay Expander
3. Film & TV Character Continuity Director
4. Film & TV Visual Beat Planner
5. Film & TV Storyboard Director
6. Film & TV Seed Image Prompt Engineer
7. Film & TV WAN I2V Director and Film & TV Motion Reference Director
8. Film & TV LTX2 Prompt Compiler
9. Film & TV Dialogue & Audio Beat Planner
10. Film & TV Model Router & Render Dispatcher
11. Film & TV Stitch Editor
12. Film & TV Continuity Reality Checker
13. Film & TV AI Orchestrator for gate control, recovery, and delivery readiness

## Design Principles

- Canon before prompt volume.
- Continuity locks before render volume.
- Model syntax should never overwrite story intent.
- Every artifact must be reusable by the next stage without re-reading the whole screenplay.
- Default to deterministic, inspectable intermediate files over hidden prompt chains.
