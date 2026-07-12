# Writerly Moves --- Scope Addendum: Connected Physical Cards

**Status:** Post-MVP Exploration **Priority:** Future Roadmap (Phase 3+)

## Vision

Augment the physical Writerly Moves card deck with embedded technology
that connects cards to dynamic digital experiences.

The goal is to make the deck feel like "living paper" while preserving
the tactile value of physical cards.

## Recommended Approach

Implement **NFC-enabled cards with QR fallback.**

Each card contains:

-   Embedded NFC tag (recommended: NTAG213)
-   Small QR code as a backup access method
-   Short printed URL or card code for manual access

All three methods point to the same cloud destination.

## User Experience

A learner taps a card with a phone and immediately accesses:

-   Audio narration of the move
-   Examples from published texts
-   Student examples
-   Revision prompts
-   Workshop activities
-   Accessibility features
-   Reflection prompts
-   App deep links
-   Instructor notes

## Why NFC Instead of Bluetooth

Bluetooth was considered but rejected for the following reasons:

-   Requires a battery
-   Increases cost and thickness
-   Creates pairing and permissions friction
-   Introduces maintenance concerns

NFC provides a simpler, more reliable classroom experience.

## Accessibility Benefits

-   Reduces visual demands
-   Enables instant audio support
-   Supports low-vision users
-   Preserves clean card design
-   Reduces reliance on camera scanning

## Technical Architecture

Physical Card -> NFC/QR -> Cloud URL -> Writerly Moves Platform

Example:

writermoves.app/card/micro-tension

## MVP Boundary

This feature is explicitly **out of scope for the initial MVP.**

The MVP should validate:

1.  Core Writerly Moves taxonomy
2.  Student engagement
3.  Workshop workflows
4.  AI-assisted reflection
5.  Instructor value

Connected cards should be explored only after product-market fit is
established.

## Trigger for Reconsideration

Revisit this feature when:

-   The card taxonomy stabilizes
-   The digital platform is operational
-   Users demonstrate demand for physical decks
-   Accessibility testing confirms added value
-   Manufacturing costs become viable
