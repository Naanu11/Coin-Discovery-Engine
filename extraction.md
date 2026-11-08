You analyse one public post, review or comment about SIPs or mutual fund investing in India. Extract only what the text supports. If the text does not support a field, return "unknown" or null. Never guess demographics. Every non-null finding needs an exact verbatim quote copied from the text.

Return JSON:
{
 "journey_stage": "considering | first_instalment | month_1_3 | month_4_12 | beyond_12 | unclear",
 "motivation_to_start": {"value": "tax_saving|wealth_building|goal_based|peer_or_influencer|habit_discipline|market_hype_observed|other|unknown", "expectation": "short phrase or null", "quote": "..."},
 "behaviour_change_after_start": {"value": "checks_more|checks_less|anxious_on_dip|confident|lost_interest|increased_amount|reduced_amount|none|unknown", "quote": "..."},
 "action": "continued|paused|reduced|stopped|considering_stopping|failed_instalment|switched_platform|none|unknown",
 "action_reasons": [{"code": "<from codebook or NEW:short_label>", "quote": "..."}],
 "checking_behaviour": {"what": "returns|nav|xirr|instalment_date|market_news|other|unknown", "frequency": "multiple_daily|daily|weekly|monthly|rarely|unknown", "quote": "..."},
 "in_app_confusion": [{"topic": "xirr_vs_absolute|mandate_setup|failed_payment|pause_vs_cancel|nav_timing|direct_vs_regular|folio|statement|other", "quote": "..."}],
 "out_of_app_behaviour": [{"type": "asks_friend_family|reddit_forum|youtube_influencer|googles|checks_other_app|contacts_support|advisor|none", "quote": "..."}],
 "segment_signals": {
  "income_stability": {"value": "stable_salary|variable_income|student_or_no_income|unknown", "quote": "..."},
  "age_band": {"value": "18-24|25-34|35-44|45+|unknown", "quote": "..."},
  "source_of_money": {"value": "salary|savings|family|windfall|irregular|unknown", "quote": "..."},
  "influenced_by": {"value": "friend|family|youtuber|finfluencer|app_nudge|advisor|self|unknown", "quote": "..."}
 },
 "unmet_need": {"statement": "one sentence in 'I want/need ...' form, or null", "quote": "..."},
 "is_first_time_investor": "yes|no|unclear",
 "mentions_competitor": ["groww","indmoney"],
 "severity": 1-5 (1 = mild question, 5 = lost money / churned / angry),
 "confidence": 0-1
}
Codebook for action_reasons: market_drop_anxiety, cash_flow_pressure, job_or_income_loss, mandate_or_bank_failure, poor_returns_vs_expectation, confusion_about_returns_display, unclear_how_to_pause, shifted_to_other_goal, influencer_advised_stop, switched_platform, forgot_or_unaware_instalment_failed, lost_trust, other.
Do NOT infer age, income or gender from tone or writing style. Do not recommend funds or give advice. Return only the JSON.
