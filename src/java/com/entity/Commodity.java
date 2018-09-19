/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.entity;

import java.io.Serializable;
import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinColumns;
import javax.persistence.Lob;
import javax.persistence.ManyToOne;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;

/**
 *
 * @author agno3
 */
@Entity
@Table(name = "commodity")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "Commodity.findAll", query = "SELECT c FROM Commodity c")
    , @NamedQuery(name = "Commodity.findByCommId", query = "SELECT c FROM Commodity c WHERE c.commId = :commId")
    , @NamedQuery(name = "Commodity.findByCommType", query = "SELECT c FROM Commodity c WHERE c.commType = :commType")
    , @NamedQuery(name = "Commodity.findByCommStartprice", query = "SELECT c FROM Commodity c WHERE c.commStartprice = :commStartprice")
    , @NamedQuery(name = "Commodity.findByCommSellprice", query = "SELECT c FROM Commodity c WHERE c.commSellprice = :commSellprice")
    , @NamedQuery(name = "Commodity.findByCommImg", query = "SELECT c FROM Commodity c WHERE c.commImg = :commImg")
    , @NamedQuery(name = "Commodity.findByCommName", query = "SELECT c FROM Commodity c WHERE c.commName = :commName")
    , @NamedQuery(name = "Commodity.findByCommCon", query = "SELECT c FROM Commodity c WHERE c.commCon = :commCon")})
public class Commodity implements Serializable {

    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 200)
    @Column(name = "comm_id")
    private String commId;
    @Basic(optional = false)
    @NotNull
    @Column(name = "comm_type")
    private int commType;
    @Lob
    @Size(max = 65535)
    @Column(name = "comm_info")
    private String commInfo;
    @Column(name = "comm_startprice")
    private Integer commStartprice;
    @Column(name = "comm_sellprice")
    private Integer commSellprice;
    @Size(max = 200)
    @Column(name = "comm_img")
    private String commImg;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 45)
    @Column(name = "comm_name")
    private String commName;
    @Lob
    @Size(max = 65535)
    @Column(name = "comm_expert_evaluation")
    private String commExpertEvaluation;
    @Column(name = "comm_con")
    private Integer commCon;
    @JoinColumns({
        @JoinColumn(name = "classification_user_user_id", referencedColumnName = "user_user_id")
        , @JoinColumn(name = "classification_class_id", referencedColumnName = "class_id")})
    @ManyToOne(optional = false)
    private Classification classification;

    public Commodity() {
    }

    public Commodity(String commId) {
        this.commId = commId;
    }

    public Commodity(String commId, int commType, String commName) {
        this.commId = commId;
        this.commType = commType;
        this.commName = commName;
    }

    public String getCommId() {
        return commId;
    }

    public void setCommId(String commId) {
        this.commId = commId;
    }

    public int getCommType() {
        return commType;
    }

    public void setCommType(int commType) {
        this.commType = commType;
    }

    public String getCommInfo() {
        return commInfo;
    }

    public void setCommInfo(String commInfo) {
        this.commInfo = commInfo;
    }

    public Integer getCommStartprice() {
        return commStartprice;
    }

    public void setCommStartprice(Integer commStartprice) {
        this.commStartprice = commStartprice;
    }

    public Integer getCommSellprice() {
        return commSellprice;
    }

    public void setCommSellprice(Integer commSellprice) {
        this.commSellprice = commSellprice;
    }

    public String getCommImg() {
        return commImg;
    }

    public void setCommImg(String commImg) {
        this.commImg = commImg;
    }

    public String getCommName() {
        return commName;
    }

    public void setCommName(String commName) {
        this.commName = commName;
    }

    public String getCommExpertEvaluation() {
        return commExpertEvaluation;
    }

    public void setCommExpertEvaluation(String commExpertEvaluation) {
        this.commExpertEvaluation = commExpertEvaluation;
    }

    public Integer getCommCon() {
        return commCon;
    }

    public void setCommCon(Integer commCon) {
        this.commCon = commCon;
    }

    public Classification getClassification() {
        return classification;
    }

    public void setClassification(Classification classification) {
        this.classification = classification;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (commId != null ? commId.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof Commodity)) {
            return false;
        }
        Commodity other = (Commodity) object;
        if ((this.commId == null && other.commId != null) || (this.commId != null && !this.commId.equals(other.commId))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "com.entity.Commodity[ commId=" + commId + " ]";
    }
    
}
