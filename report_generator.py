def generate_report(result):

    risk_level ="LOW"

    if result["tampering_suspected"]:
        risk_level ="MEDIUM"

    if result["blur_score"]<30:
        risk_level ="HIGH"

    report = {
        "document_quality":{"blur_score": result["blur_score"],"edge_score": result["edge_score"]},

        "text_extraction_preview":result["extracted_text"],

        "tampering_analysis":{"suspected": result["tampering_suspected"]},

        "fraud_risk_assessment": risk_level
    }

    return report